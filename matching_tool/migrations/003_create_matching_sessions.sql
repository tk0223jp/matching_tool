-- migrations/003_create_matching_sessions.sql
-- Issue #3: matching_sessions テーブルの作成

CREATE TABLE IF NOT EXISTS matching_sessions (
    id           INTEGER  PRIMARY KEY AUTOINCREMENT,
    trigger_type TEXT     NOT NULL CHECK(trigger_type IN ('MANUAL', 'AUTO')),
    memo         TEXT,
    created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- updated_at を自動更新するトリガー
CREATE TRIGGER IF NOT EXISTS trg_matching_sessions_updated_at
AFTER UPDATE ON matching_sessions
FOR EACH ROW
BEGIN
    UPDATE matching_sessions
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = OLD.id;
END;