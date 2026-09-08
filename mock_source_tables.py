"""
mock_source_tables.py

Plain pd.DataFrame() literals for every table referenced by the segment
analysis queries.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# DataFrames Definitions
# ---------------------------------------------------------------------------

summary_kb__AUM_loan_snapshot_2_res_3 = pd.DataFrame({
    "loan_id":       ["KB0001", "KB0002", "KB0003", "KB0004", "KB0005", "KB0006"],
    "purchaseid":    ["KBP0001", "KBP0002", "KBP0003", "KBP0004", "KBP0005", "KBP0006"],
    "snapshot_date": ["2026-07-31", "2026-07-31", "2026-08-31", "2026-08-31", "2026-08-31", "2026-07-31"],
    "product_name":  ["EDI", "CARD", "EDI", "CARD", "PL", "PL"],
    "kbnbfc_pos":    [125000.50, 43000.00, 132500.75, 45200.00, 98000.00, 87000.00],
    "partner_pos":   [30000.00, 0.00, 31000.00, 0.00, 15000.00, 12000.00],
})

findata_kb__yp_loan_dimensional_tbl = pd.DataFrame({
    "loan_id":          ["KB0001", "KB0002", "KB0003", "KB0004", "KB0005", "KB0006"],
    "purchase_id":      ["KBP0001", "KBP0002", "KBP0003", "KBP0004", "KBP0005", "KBP0006"],
    "erp_product_name": ["EDI", "CARD", "EDI", "CARD", "PL", "PL"],
    "product_name":     ["EDI", "CARD", "EDI", "CARD", "PL", "PL"],
})

summary_kz__AUM_loan_snapshot_2_res_3 = pd.DataFrame({
    "snapshot_date": ["2026-07-31", "2026-07-31", "2026-08-31", "2026-08-31"],
    "fund_name":     ["KB", "KBP", "KB", "OTHER"],
    "pos":           [220000.00, 95000.00, 231000.00, 40000.00],
})

# Single paid_date column used consistently
findata_kb__offline_loandata_tbl = pd.DataFrame({
    "Curr_New_Account_No": ["OFF001", "OFF002", "OFF003", "OFF004", "OFF005"],
    "disbursed_date":      ["2026-08-02", "2026-08-05", "2026-08-10", "2026-07-20", "2026-08-15"],
    "paid_date":          ["2026-08-20", None, "2026-08-25", "2026-08-11", None],
    "principal":          [50000.00, 75000.00, 30000.00, 62000.00, 41000.00],
    "principalpaid":      [12000.00, 0.00, 30000.00, 62000.00, 5000.00],
})

summary_kb__DBL_LAP_offline_aum_loan_snapshot = pd.DataFrame({
    "loan_id":       ["LAP0001", "LAP0002", "LAP0003", "LAP0004", "LAP0005"],
    "snapshot_date": ["2026-07-31", "2026-07-31", "2026-08-31", "2026-08-31", "2026-08-31"],
    "platform":      ["DBL_LAP_TWL_POPSA_SCF"] * 5,
    "kbnbfc_pos":    [560000.00, 210000.00, 575000.00, 220000.00, 98000.00],
})

findata_dbl__yp_loan_dimensional_tbl = pd.DataFrame({
    "loan_id":          ["LAP0001", "LAP0002", "LAP0003", "LAP0004", "LAP0005"],
    "erp_product_name": ["DBL", "TWL", "DBL", "POPSA", "MICRO_LAP"],
    "product_name":     ["DBL", "TWL", "DBL", "POPSA", "MICRO_LAP"],
})

findata_kb__yp_emi_data_tbl = pd.DataFrame({
    "loan_id":                         ["KB0001", "KB0002", "KB0003", "KB0004", "KB0005"],
    "installment_number":              [1, 1, 1, 2, 1],
    "disbursed_date":                  ["2026-08-01", "2026-08-05", "2026-08-10", "2026-08-10", "2026-08-20"],
    "kbnbfc_principaldue":             [20000.00, 15000.00, 18000.00, 5000.00, 22000.00],
    "partner_principaldue":            [8000.00, 5000.00, 6000.00, 2000.00, 9000.00],
    "state":                           ["disbursed", "closed", "disbursed", "disbursed", "disbursed"],
    "kbnbfc_fund_allocation_percent":  [60, 55, 70, 70, 40],
})

findata_dbl__yp_emi_data_tbl = pd.DataFrame({
    "loan_id":               ["LAP0001", "LAP0002", "LAP0003", "LAP0004", "LAP0005"],
    "installment_number":   [1, 1, 1, 1, 2],
    "disbursed_date":       ["2026-08-03", "2026-08-06", "2026-08-12", "2026-08-18", "2026-08-18"],
    "principaldue":         [40000.00, 12000.00, 35000.00, 9000.00, 3000.00],
})

findata_dbl__yp_loan = pd.DataFrame({
    "id":       [1, 2, 3, 4, 5],
    "kbloanid": ["LAP0001", "LAP0002", "LAP0003", "LAP0004", "LAP0005"],
})

findata_dbl__yp_tranche_disbursals = pd.DataFrame({
    "loanid":          [1, 2, 3, 4, 5],
    "trancheNo":       [1, 1, 1, 2, 1],
    "disbursedon":     ["2026-08-01 04:00:00", "2026-08-05 05:00:00", "2026-08-12 06:00:00",
                        "2026-08-18 07:00:00", "2026-08-25 03:00:00"],
    "amount":          [500000.00, 210000.00, 350000.00, 90000.00, 60000.00],
    "agreementFees":   [2000.00, 1000.00, 1500.00, 0.00, 500.00],
    "processingFees":  [3000.00, 1500.00, 2000.00, 0.00, 700.00],
    "insuranceFee":    [500.00, 300.00, 400.00, 0.00, 100.00],
    "gstFees":         [900.00, 450.00, 700.00, 0.00, 200.00],
    "state":           [87, 87, 87, 87, 87],
})

findata_kb__yp_collections_data_tbl = pd.DataFrame({
    "loanid":                  ["KB0001", "KB0002", "KB0003", "KB0004", "KB0005"],
    "txndate":                 ["2026-08-02", "2026-08-06", "2026-08-11", "2026-08-15", "2026-08-22"],
    "kbnbfc_principal_paid":   [3000.00, 4200.00, 2800.00, 5100.00, 3600.00],
    "partner_principal_paid":  [1200.00, 1800.00, 900.00, 2000.00, 1500.00],
})

findata_kb__card_new_recon = pd.DataFrame({
    "principal_paid_date": ["2026-08-03", "2026-08-09", "2026-08-14", "2026-08-19"],
    "purchase_type":       ["purchase", "bankWithdrawal", "purchase", "other"],
    "principal_paid":      [2200.00, 3100.00, 1800.00, 900.00],
})

findata_kz__yp_emi_data_tbl = pd.DataFrame({
    "emi_partital_paid_date": ["2026-08-02 10:00:00", "2026-08-07 10:00:00", "2026-08-16 10:00:00"],
    "principal_paid":         [4000.00, 5200.00, 3100.00],
    "fund_name":              ["KB", "KBP", "OTHER"],
})

findata_dbl__yp_collections_data_tbl = pd.DataFrame({
    "loanid":         ["LAP0001", "LAP0002", "LAP0003", "LAP0004"],
    "txndate":        ["2026-08-04", "2026-08-09", "2026-08-17", "2026-08-23"],
    "principal_paid": [9000.00, 6200.00, 7800.00, 4100.00],
})

findata_stu__temp_all_emi_all_vw = pd.DataFrame({
    "paiddate":      ["2026-07-15 09:00:00", "2026-08-02 09:00:00", "2026-08-18 09:00:00", "2026-08-27 09:00:00"],
    "PrincipalPaid": [3000.00, 2500.00, 4100.00, 1900.00],
    "fund_name":     ["KBNBFC", "KBNBFC", "OTHER", "KBNBFC"],
    "OrderID":       ["ORD001", "ORD002", "ORD003", "ORD004"],
})

findata_kb__yp_loan_installments = pd.DataFrame({
    "loanid": ["KB0001", "KB0001", "KB0002", "KB0003", "KB0003", "KB0003"],
    "id":     [1, 2, 3, 4, 5, 6],
})

findata_kz__yp_loan = pd.DataFrame({
    "id":          [1, 2, 3],
    "productname": ["KZ_A", "KZ_B", "KZ_A"],
})

findata_kz__yp_loan_installments = pd.DataFrame({
    "loanid": [1, 1, 2, 3, 3],
    "id":     [101, 102, 103, 104, 105],
})

findata_dbl__yp_loan_installments = pd.DataFrame({
    "loanid": ["LAP0001", "LAP0001", "LAP0002", "LAP0003", "LAP0004"],
    "id":     [201, 202, 203, 204, 205],
})

kreditbee_bi_dw_athena__kb_aum_loan_snapshot_archived = pd.DataFrame({
    "loan_id":                    ["KB0001", "KB0002", "KB0003", "KB0004", "KB0005", "KB0001", "KB0002"],
    "snapshot_date":              ["2026-08-01", "2026-08-01", "2026-08-01", "2026-08-15", "2026-08-15",
                                   "2026-08-31", "2026-08-31"],
    "pos":                        [125000.00, 43000.00, 98000.00, 130000.00, 44000.00, 132500.00, 45200.00],
    "pan_level_aum_kbnbfc":       [110000.00, 40000.00, 90000.00, 115000.00, 41000.00, 118000.00, 42000.00],
    "da_assignee_pan_level_aum":  [20000.00, 5000.00, 10000.00, 21000.00, 5200.00, 22000.00, 5300.00],
})

kreditbee_bi_dw_athena__offline_aum_loan_snapshot_archived = pd.DataFrame({
    "loan_id":               ["LAP0001", "LAP0002", "LAP0003", "LAP0004", "LAP0001", "LAP0002"],
    "snapshot_date":         ["2026-08-01", "2026-08-01", "2026-08-01", "2026-08-15", "2026-08-31", "2026-08-31"],
    "pos":                   [560000.00, 210000.00, 98000.00, 220000.00, 575000.00, 215000.00],
    "pan_level_aum_kbnbfc":  [540000.00, 205000.00, 95000.00, 218000.00, 555000.00, 209000.00],
})

# ---------------------------------------------------------------------------
# Dynamic Schema Mappings (Including Previous Month / July Schemas)
# ---------------------------------------------------------------------------
TABLES = {
    # Summary Tables
    "summary_kb.AUM_loan_snapshot_2_res_3": summary_kb__AUM_loan_snapshot_2_res_3,
    "summary_kz.AUM_loan_snapshot_2_res_3": summary_kz__AUM_loan_snapshot_2_res_3,
    "summary_kb.DBL_LAP_offline_aum_loan_snapshot": summary_kb__DBL_LAP_offline_aum_loan_snapshot,
    "kreditbee_bi_dw_athena.kb_aum_loan_snapshot_archived": kreditbee_bi_dw_athena__kb_aum_loan_snapshot_archived,
    "kreditbee_bi_dw_athena.offline_aum_loan_snapshot_archived": kreditbee_bi_dw_athena__offline_aum_loan_snapshot_archived,

    # Current Month Schemas (August 2026)
    "findata_kb_31_08_2026.yp_loan_dimensional_tbl": findata_kb__yp_loan_dimensional_tbl,
    "findata_kb_31_08_2026.offline_loandata_tbl": findata_kb__offline_loandata_tbl,
    "findata_dbl_lap_31_08_2026.yp_loan_dimensional_tbl": findata_dbl__yp_loan_dimensional_tbl,
    "findata_kb_31_08_2026.yp_emi_data_tbl": findata_kb__yp_emi_data_tbl,
    "findata_dbl_lap_31_08_2026.yp_emi_data_tbl": findata_dbl__yp_emi_data_tbl,
    "findata_dbl_lap_31_08_2026.yp_loan": findata_dbl__yp_loan,
    "findata_dbl_lap_31_08_2026.yp_tranche_disbursals": findata_dbl__yp_tranche_disbursals,
    "findata_kb_31_08_2026.yp_collections_data_tbl": findata_kb__yp_collections_data_tbl,
    "findata_kb_31_08_2026.card_new_recon": findata_kb__card_new_recon,
    "findata_kz_31_08_2026.yp_emi_data_tbl": findata_kz__yp_emi_data_tbl,
    "findata_dbl_lap_31_08_2026.yp_collections_data_tbl": findata_dbl__yp_collections_data_tbl,
    "findata_stu_31_08_2026.temp_all_emi_all_vw": findata_stu__temp_all_emi_all_vw,
    "findata_kb_31_08_2026.yp_loan_installments": findata_kb__yp_loan_installments,
    "findata_kz_31_08_2026.yp_loan": findata_kz__yp_loan,
    "findata_kz_31_08_2026.yp_loan_installments": findata_kz__yp_loan_installments,
    "findata_dbl_lap_31_08_2026.yp_loan_installments": findata_dbl__yp_loan_installments,

    # Previous Month Schemas (July 2026 Mapping for Mock Execution)
    "findata_kb_31_07_2026.yp_loan_dimensional_tbl": findata_kb__yp_loan_dimensional_tbl,
    "findata_kb_31_07_2026.offline_loandata_tbl": findata_kb__offline_loandata_tbl,
    "findata_dbl_lap_31_07_2026.yp_loan_dimensional_tbl": findata_dbl__yp_loan_dimensional_tbl,
}