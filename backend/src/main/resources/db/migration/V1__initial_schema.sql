CREATE TABLE roles (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(320) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    display_name VARCHAR(120) NOT NULL,
    role_id BIGINT NOT NULL REFERENCES roles(id),
    active BOOLEAN NOT NULL DEFAULT TRUE,
    last_login_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE scan_history (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(id),
    source_text TEXT NOT NULL,
    verdict VARCHAR(32) NOT NULL,
    risk_score SMALLINT,
    scanned_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE whitelist_entries (
    id BIGSERIAL PRIMARY KEY,
    entry_value VARCHAR(512) NOT NULL UNIQUE,
    entry_type VARCHAR(32) NOT NULL,
    reason VARCHAR(255),
    created_by_user_id BIGINT REFERENCES users(id),
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE blacklist_entries (
    id BIGSERIAL PRIMARY KEY,
    entry_value VARCHAR(512) NOT NULL UNIQUE,
    entry_type VARCHAR(32) NOT NULL,
    reason VARCHAR(255),
    created_by_user_id BIGINT REFERENCES users(id),
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_role_id ON users(role_id);
CREATE INDEX idx_scan_history_user_id ON scan_history(user_id);
CREATE INDEX idx_scan_history_scanned_at ON scan_history(scanned_at DESC);
CREATE INDEX idx_whitelist_entry_type ON whitelist_entries(entry_type);
CREATE INDEX idx_blacklist_entry_type ON blacklist_entries(entry_type);
