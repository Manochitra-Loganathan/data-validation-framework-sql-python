
-- Null Check for Required Fields
SELECT COUNT(*) AS NullCount
FROM staging.sales_data
WHERE customer_id IS NULL OR product_id IS NULL;

-- Row Count Reconciliation
SELECT 'Staging Count' AS Source, COUNT(*) AS RowCount FROM staging.sales_data
UNION ALL
SELECT 'Reporting Count' AS Target, COUNT(*) FROM reporting.sales_summary;
