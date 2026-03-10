-- migrations/005_create_system_b_records.sql
-- Issue #5: system_b_records テーブルの作成

CREATE TABLE IF NOT EXISTS system_b_records (
    id              INTEGER  PRIMARY KEY AUTOINCREMENT,
    session_id      INTEGER  NOT NULL
                             REFERENCES matching_sessions(id)
                             ON DELETE CASCADE
                             ON UPDATE CASCADE,
    approval_number TEXT     NOT NULL,
    upper_limit     REAL     NOT NULL,
    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- updated_at を自動更新するトリガー
CREATE TRIGGER IF NOT EXISTS trg_system_b_records_updated_at
AFTER UPDATE ON system_b_records
FOR EACH ROW
BEGIN
    UPDATE system_b_records
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = OLD.id;
END;