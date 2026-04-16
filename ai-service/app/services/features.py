from dataclasses import dataclass
import ipaddress
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = ("login", "verify", "secure", "update", "account", "banking")


@dataclass
class UrlFeatures:
    url_length: int
    domain_length: int
    dot_count: int
    hyphen_count: int
    digit_count: int
    host_is_ip: bool
    suspicious_keywords: list[str]


def _extract_host(url: str) -> str:
    return (urlparse(url).hostname or "").lower()


def _is_ip_address(host: str) -> bool:
    if not host:
        return False
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def extract_features(url: str) -> UrlFeatures:
    host = _extract_host(url)
    full = url.lower()

    matches = [kw for kw in SUSPICIOUS_KEYWORDS if kw in full]

    return UrlFeatures(
        url_length=len(url),
        domain_length=len(host),
        dot_count=host.count("."),
        hyphen_count=host.count("-"),
        digit_count=sum(ch.isdigit() for ch in host),
        host_is_ip=_is_ip_address(host),
        suspicious_keywords=matches,
    )
