ALTER TABLE scan_history
    ADD COLUMN scanned_url VARCHAR(2048);

UPDATE scan_history
SET scanned_url = LEFT(source_text, 2048)
WHERE scanned_url IS NULL;

ALTER TABLE scan_history
    ALTER COLUMN scanned_url SET NOT NULL,
    ALTER COLUMN risk_score TYPE NUMERIC(5,2) USING risk_score::NUMERIC(5,2),
    ADD COLUMN confidence NUMERIC(5,4),
    ADD COLUMN explanations TEXT,
    DROP COLUMN source_text;

ALTER TABLE scan_history
    ADD CONSTRAINT chk_scan_history_verdict
        CHECK (verdict IN ('SAFE', 'SUSPICIOUS', 'DANGEROUS'));

ALTER TABLE whitelist_entries
    ADD CONSTRAINT chk_whitelist_entry_type
        CHECK (entry_type IN ('DOMAIN', 'EMAIL', 'URL', 'IP'));

ALTER TABLE blacklist_entries
    ADD CONSTRAINT chk_blacklist_entry_type
        CHECK (entry_type IN ('DOMAIN', 'EMAIL', 'URL', 'IP'));

CREATE INDEX idx_scan_history_scanned_url ON scan_history(scanned_url);
