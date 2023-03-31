BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS 'currency' (
    'code'      TEXT,
    'name'      text,
    'symbol'    text,
    PRIMARY KEY ('code')
);

COMMIT;
