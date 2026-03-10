-- migrations/004_create_system_a_records.sql
-- Issue #4: system_a_records テーブルの作成

CREATE TABLE IF NOT EXISTS system_a_records (
    id              INTEGER  PRIMARY KEY AUTOINCREMENT,
    session_id      INTEGER  NOT NULL
                             REFERENCES matching_sessions(id)
                             ON DELETE CASCADE
                             ON UPDATE CASCADE,
    approval_number TEXT     NOT NULL,
    supplier_code   TEXT     NOT NULL,
    amount          REAL     NOT NULL,
    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- updated_at を自動更新するトリガー
CREATE TRIGGER IF NOT EXISTS trg_system_a_records_updated_at
AFTER UPDATE ON system_a_records
FOR EACH ROW
BEGIN
    UPDATE system_a_records
    SET updated_at = CURRENT_TIMESTAMP
    WHERE id = OLD.id;
END;