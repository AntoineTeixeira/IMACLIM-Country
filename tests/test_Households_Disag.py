# coding: utf-8

from src import Households_disag as hhd
import numpy as np
import pandas as pd


expected_disagggregated_account_table_data = np.array([[ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  5.2510731e+07],
                                                       [ 4.0660000e+08,  5.7863601e+07,  7.3052558e+06,  7.7055627e+06,  8.4946046e+06,  1.0879671e+07,  1.2195411e+07,  1.4493760e+07,  1.6660707e+07,  1.9626821e+07,  2.2088885e+07,  3.4393607e+07,  0.0000000e+00],
                                                       [ 0.0000000e+00,  0.0000000e+00,  8.1879758e+06,  2.2792715e+07,  3.0783332e+07,  4.4449379e+07,  5.4585017e+07,  7.0400939e+07,  8.2849467e+07,  9.9795474e+07,  1.1280000e+08,  2.1380000e+08,  0.0000000e+00],
                                                       [ 0.0000000e+00,  3.2530000e+08,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
                                                       [ 0.0000000e+00,  5.7305585e+07,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
                                                       [ 0.0000000e+00,  2.3577000e+07,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
                                                       [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
                                                       [ 0.0000000e+00,  3.6613000e+07,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
                                                       [ 0.0000000e+00,  1.3560000e+08,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
                                                       [-6.8823000e+07, -3.1360000e+07,  3.9341830e+06,  5.2816951e+06, 6.1300729e+06,  8.3192851e+06,  8.5513854e+06,  1.4654525e+07, 1.5910991e+07,  1.6981023e+07,  1.6293756e+07,  2.7065084e+07,-2.2939000e+07],
                                                       [ 0.0000000e+00, -4.2550000e+07,  3.0801368e+06,  4.5758637e+06,  4.9921092e+06,  4.4245956e+06,  4.5088684e+06,  3.6838409e+06,  3.9128060e+06,  3.9438173e+06,  4.2826917e+06,  5.1452705e+06,  0.0000000e+00],
                                                       [ 0.0000000e+00, -2.7850000e+08,  5.5709344e+06,  1.6028946e+07,  2.3257374e+07,  2.5555126e+07,  2.7400660e+07,  2.7204504e+07,  2.9242334e+07,  3.1222362e+07,  4.0332561e+07,  5.2728198e+07,  0.0000000e+00],
                                                       [ 0.0000000e+00, -9.4245000e+07,  1.9989020e+07,  1.9519940e+07,  1.3394127e+07,  9.7216441e+06,  7.7979984e+06,  6.7230803e+06,  5.7139057e+06,  5.0734398e+06,  3.5807595e+06,  2.7310862e+06,  0.0000000e+00],
                                                       [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
                                                       [-9.0502429e+07,  5.8083617e+07,  1.1785684e+06,  1.6091610e+06, 1.8540870e+06,  2.2628457e+06,  2.4168809e+06,  2.3783260e+06, 2.5115989e+06,  2.8386989e+06,  3.4060831e+06,  4.4000110e+06, 7.5625502e+06],
                                                       [ 0.0000000e+00,  1.4260000e+08, -2.0132975e+05, -7.2928393e+05, -9.8300144e+05, -1.6882113e+06, -2.6908255e+06, -5.6570533e+06, -8.5489043e+06, -1.4463729e+07, -2.3183890e+07, -8.4487772e+07,  0.0000000e+00],
                                                       [-3.6683000e+07,  3.6683000e+07,  0.0000000e+00,  0.0000000e+00, 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00, 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00, 0.0000000e+00],
                                                       [ 0.0000000e+00,  2.1618000e+07, -7.4705400e+05, -9.3881814e+05, -1.0355949e+06, -1.5169287e+06, -1.8072420e+06, -2.1382738e+06, -2.4219076e+06, -2.7188031e+06, -3.3485272e+06, -4.9448505e+06,  0.0000000e+00],
                                                       [ 2.1060000e+08,  4.4860000e+08,  4.8297690e+07,  7.5845780e+07,  8.6887110e+07,  1.0240000e+08,  1.1300000e+08,  1.3170000e+08,  1.4580000e+08,  1.6230000e+08,  1.7630000e+08,  2.5080000e+08,  3.7134281e+07],
                                                       [ 0.0000000e+00,  5.2160000e+08,  6.6357036e+07,  7.2940179e+07,  8.0739106e+07,  9.0990748e+07,  9.7307415e+07,  1.0730000e+08,  1.1600000e+08,  1.2920000e+08,  1.4340000e+08,  1.8710000e+08,  0.0000000e+00],
                                                       [ 2.0010000e+08,  6.4284000e+07,  4.6040968e+06,  5.5446290e+06,  2.8273718e+06,  3.0619761e+06,  6.7941455e+06,  1.1065056e+07,  1.0312878e+07,  2.0227705e+07,  2.2349911e+07,  2.5524231e+07,  0.0000000e+00],
                                                       [ 2.0010000e+08,  5.8590000e+08,  7.0961133e+07,  7.8484808e+07,  8.3566477e+07,  9.4052724e+07,  1.0410000e+08,  1.1830000e+08,  1.2630000e+08,  1.4940000e+08,  1.6580000e+08,  2.1260000e+08,  0.0000000e+00],
                                                       [ 1.0505453e+07, -1.3740000e+08, -2.2663443e+07, -2.6390274e+06,  3.3206328e+06,  8.3546831e+06,  8.8565936e+06,  1.3422460e+07,  1.9540938e+07,  1.2851434e+07,  1.0474988e+07,  3.8215007e+07,  3.7134281e+07],
                                                       [ 1.9110000e+09,  1.0680000e+09, -8.3851186e+07, -1.1260000e+08, -1.3070000e+08, -1.7730000e+08, -1.8230000e+08, -3.1230000e+08, -3.3910000e+08, -3.6190000e+08, -3.4730000e+08, -5.7690000e+08, -3.5470000e+08]])
expected_disagggregated_account_table_index = ['Trade_Balance', 'GOS_byAgent', 'NetCompWages_byAgent',
                                               'InsuranceContrib_byAgent', 'Production_Tax_byAgent',
                                               'Energ_Tax_byAgent', 'Carbon_Tax_byAgent', 'OtherIndirTax_byAgent',
                                               'VA_Tax_byAgent', 'Property_income', 'Unemployment_transfers',
                                               'Pensions', 'Other_social_transfers', 'ClimPolicyCompens',
                                               'Other_Transfers', 'Income_Tax', 'Corporate_Tax', 'Other_Direct_Tax',
                                               'Disposable_Income', 'FC_byAgent', 'GFCF_byAgent', 'Tot_FC_byAgent',
                                               'NetLending', 'NetFinancialDebt']
expected_disagggregated_account_table_columns = ['Corporations', 'Government', 'H1', 'H2',
                                                 'H3', 'H4', 'H5', 'H6',
                                                 'H7', 'H8', 'H9', 'H10',
                                                 'RestOfWorld']
expected_disagggregated_account_table = pd.DataFrame(expected_disagggregated_account_table_data,
                                                     index=expected_disagggregated_account_table_index,
                                                     columns=expected_disagggregated_account_table_columns)


account_data_data = np.array([[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  5.25107308e+07],
                              [ 4.06638882e+08,  5.78636011e+07,  1.53844284e+08,  0.00000000e+00],
                              [ 0.00000000e+00,  0.00000000e+00,  7.40467720e+08,  0.00000000e+00],
                              [ 0.00000000e+00,  3.25294206e+08,  0.00000000e+00,  0.00000000e+00],
                              [ 0.00000000e+00,  5.73055854e+07,  0.00000000e+00,  0.00000000e+00],
                              [ 0.00000000e+00,  2.35770000e+07,  0.00000000e+00,  0.00000000e+00],
                              [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
                              [ 0.00000000e+00,  3.66130000e+07,  0.00000000e+00,  0.00000000e+00],
                              [ 0.00000000e+00,  1.35578990e+08,  0.00000000e+00,  0.00000000e+00],
                              [-6.88230000e+07, -3.13600000e+07,  1.23122000e+08, -2.29390000e+07],
                              [ 0.00000000e+00, -4.25500000e+07,  4.25500000e+07,  0.00000000e+00],
                              [ 0.00000000e+00, -2.78543000e+08,  2.78543000e+08,  0.00000000e+00],
                              [ 0.00000000e+00, -9.42450000e+07,  9.42450000e+07,  0.00000000e+00],
                              [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
                              [-9.05024286e+07,  5.80836174e+07,  2.48562610e+07,  7.56255024e+06],
                              [ 0.00000000e+00,  1.42634000e+08, -1.42634000e+08,  0.00000000e+00],
                              [-3.66830000e+07,  3.66830000e+07,  0.00000000e+00,  0.00000000e+00],
                              [ 0.00000000e+00,  2.16180000e+07, -2.16180000e+07,  0.00000000e+00],
                              [ 2.10630453e+08,  4.48553000e+08,  1.29337627e+09,  3.71342810e+07],
                              [ 0.00000000e+00,  5.21643000e+08,  1.09133000e+09,  0.00000000e+00],
                              [ 2.00125000e+08,  6.42840000e+07,  1.12312000e+08,  0.00000000e+00],
                              [ 2.00125000e+08,  5.85927000e+08,  1.20364200e+09,  0.00000000e+00],
                              [ 1.05054530e+07, -1.37374000e+08,  8.97342660e+07,  3.71342810e+07],
                              [ 1.91128800e+09,  1.06758400e+09, -2.62416000e+09, -3.54712000e+08]])
account_data_index = ['Trade_Balance', 'GOS_byAgent', 'NetCompWages_byAgent',
                      'InsuranceContrib_byAgent', 'Production_Tax_byAgent',
                      'Energ_Tax_byAgent', 'Carbon_Tax_byAgent', 'OtherIndirTax_byAgent',
                      'VA_Tax_byAgent', 'Property_income', 'Unemployment_transfers',
                      'Pensions', 'Other_social_transfers', 'ClimPolicyCompens',
                      'Other_Transfers', 'Income_Tax', 'Corporate_Tax', 'Other_Direct_Tax',
                      'Disposable_Income', 'FC_byAgent', 'GFCF_byAgent', 'Tot_FC_byAgent',
                      'NetLending', 'NetFinancialDebt']
account_data_columns = ['Corporations', 'Government', 'Households', 'RestOfWorld']
account_data = pd.DataFrame(account_data_data,
                            index=account_data_index,
                            columns=account_data_columns)


account_data_rate_data = np.array([[0.04748474, 0.05008677, 0.0552156 , 0.07071872, 0.07927113, 0.09421058, 0.10829591, 0.12757589, 0.1435795 , 0.22356116],
                                   [0.01105784, 0.03078151, 0.04157282, 0.06002879, 0.07371694, 0.09507631, 0.11188802, 0.13477356, 0.15236485, 0.28873935],
                                   [0.03195353, 0.04289806, 0.04978861, 0.06756944, 0.06945457, 0.11902442, 0.12922947, 0.1379203 , 0.1323383 , 0.2198233 ],
                                   [0.07238865, 0.10754086, 0.11732336, 0.1039858 , 0.10596635, 0.08657675, 0.09195784, 0.09268666, 0.1006508 , 0.12092293],
                                   [0.02000027, 0.05754568, 0.08349653, 0.09174571, 0.09837138, 0.09766716, 0.1049832 , 0.11209171, 0.14479833, 0.18930003],
                                   [0.21209634, 0.2071191 , 0.14212029, 0.10315289, 0.08274177, 0.0713362 , 0.06062821, 0.05383246, 0.03799416, 0.02897858],
                                   [0.        , 0.        , 0.        , 0.        , 0.        , 0.        , 0.        , 0.        , 0.        , 0.        ],
                                   [0.04741535, 0.06473866, 0.07459235, 0.09103725, 0.09723429, 0.09568318, 0.10104492, 0.11420458, 0.13703119, 0.17701822],
                                   [0.00141151, 0.00511297, 0.00689178, 0.01183597, 0.01886525, 0.03966132, 0.05993595, 0.1014045 , 0.16254112, 0.59233964],
                                   [0.03455704, 0.04342761, 0.04790429, 0.07016971, 0.08359895, 0.09891173, 0.11203199, 0.12576571, 0.15489533, 0.22873765],
                                   [0.06080382, 0.06683604, 0.0739823 , 0.08337602, 0.08916406, 0.0982802 , 0.10627141, 0.11840595, 0.1314439 , 0.17143629],
                                   [0.04099381, 0.04936809, 0.02517426, 0.02726312, 0.0604935 , 0.0985207 , 0.09182347, 0.18010279, 0.19899842, 0.22726183],
                                   [0.03195353, 0.04289806, 0.04978861, 0.06756944, 0.06945457, 0.11902442, 0.12922947, 0.1379203 , 0.1323383 , 0.2198233 ]])
account_data_rate_index = ['GOS_byAgent', 'NetCompWages_byAgent', 'Property_income',
                           'Unemployment_transfers', 'Pensions', 'Other_social_transfers',
                           'ClimPolicyCompens', 'Other_Transfers', 'Income_Tax',
                           'Other_Direct_Tax', 'FC_byAgent', 'GFCF_byAgent', 'NetFinancialDebt']
account_data_rate_columns = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10']
account_data_rate = pd.DataFrame(account_data_rate_data,
                                 index=account_data_rate_index,
                                 columns=account_data_rate_columns)

accounts_mapping = {'DataAccount': ['Trade_Balance', 'GOS_byAgent', 'NetCompWages_byAgent', 'InsuranceContrib_byAgent',
                                    'Production_Tax_byAgent', 'Energ_Tax_byAgent', 'OtherIndirTax_byAgent', 'VA_Tax_byAgent',
                                    'Property_income', 'Unemployment_transfers', 'Pensions', 'Other_social_transfers',
                                    'ClimPolicyCompens', 'Other_Transfers', 'Income_Tax', 'Corporate_Tax', 'Other_Direct_Tax',
                                    'Disposable_Income', 'FC_byAgent', 'GFCF_byAgent', 'Tot_FC_byAgent',
                                    'NetLending', 'NetFinancialDebt'],
                    'H_Income': ['GOS_byAgent', 'NetCompWages_byAgent', 'Property_income', 'Unemployment_transfers',
                                 'Pensions', 'Other_social_transfers', 'ClimPolicyCompens', 'Other_Transfers'],
                    'H_Tax': ['Income_Tax', 'Other_Direct_Tax'],
                    'H_Expenditures': ['FC_byAgent', 'GFCF_byAgent'],
                    'Corporations': ['Corporations'],
                    'DomesticAgents': ['Corporations', 'Government', 'H1', 'H2',
                                       'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10'],
                    'InstitAgents': ['Corporations', 'Government', 'H1', 'H2',
                                     'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
                                     'H10', 'RestOfWorld'],
                    'Government': ['Government'],
                    'Households': ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10'],
                    'RestOfWorld': ['RestOfWorld']}


def test_disaggregate_account_table():
    pd.testing.assert_frame_equal(hhd.disaggregate_account_table('Households',
                                                                 account_data,
                                                                 account_data_rate,
                                                                 'H10',
                                                                 accounts_mapping),
                                  expected_disagggregated_account_table,
                                  check_less_precise=True)


expected_disaggregated_households_round_erred_data = np.array([[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 7.30525585e+06,  7.70556268e+06,  8.49460463e+06, 1.08796707e+07,  1.21954109e+07,  1.44937600e+07, 1.66607069e+07,  1.96268212e+07,  2.20888850e+07, 3.43936064e+07],
                                                               [ 8.18797580e+06,  2.27927145e+07,  3.07833320e+07, 4.44493791e+07,  5.45850175e+07,  7.04009393e+07, 8.28494671e+07,  9.97954737e+07,  1.12821255e+08, 2.13802166e+08],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 3.93418301e+06,  5.28169507e+06,  6.13007287e+06, 8.31928508e+06,  8.55138544e+06,  1.46545248e+07, 1.59109908e+07,  1.69810234e+07,  1.62937558e+07, 2.70650837e+07],
                                                               [ 3.08013684e+06,  4.57586372e+06,  4.99210918e+06, 4.42459558e+06,  4.50886836e+06,  3.68384088e+06, 3.91280596e+06,  3.94381734e+06,  4.28269167e+06, 5.14527046e+06],
                                                               [ 5.57093437e+06,  1.60289458e+07,  2.32573742e+07, 2.55551264e+07,  2.74006599e+07,  2.72045040e+07, 2.92423341e+07,  3.12223623e+07,  4.03325612e+07, 5.27281977e+07],
                                                               [ 1.99890197e+07,  1.95199397e+07,  1.33941267e+07, 9.72164412e+06,  7.79799840e+06,  6.72308026e+06, 5.71390565e+06,  5.07343982e+06,  3.58075951e+06, 2.73108618e+06],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 1.17856839e+06,  1.60916103e+06,  1.85408702e+06, 2.26284572e+06,  2.41688089e+06,  2.37832602e+06, 2.51159888e+06,  2.83869892e+06,  3.40608312e+06, 4.40001101e+06],
                                                               [-2.01329745e+05, -7.29283934e+05, -9.83001435e+05, -1.68821132e+06, -2.69082550e+06, -5.65705329e+06, -8.54890429e+06, -1.44637292e+07, -2.31838895e+07, -8.44877719e+07],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [-7.47054004e+05, -9.38818138e+05, -1.03559494e+06, -1.51692870e+06, -1.80724204e+06, -2.13827380e+06, -2.42190762e+06, -2.71880305e+06, -3.34852724e+06, -4.94485045e+06],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 6.63570362e+07,  7.29401788e+07,  8.07391056e+07, 9.09907475e+07,  9.73074147e+07,  1.07256132e+08, 1.15977181e+08,  1.29219965e+08,  1.43448676e+08, 1.87093562e+08],
                                                               [ 4.60409679e+06,  5.54462904e+06,  2.82737183e+06, 3.06197609e+06,  6.79414552e+06,  1.10650563e+07, 1.03128780e+07,  2.02277050e+07,  2.23499109e+07, 2.55242304e+07],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                               [-8.38511858e+07, -1.12571376e+08, -1.30653271e+08, -1.77313032e+08, -1.82259902e+08, -3.12339125e+08, -3.39118806e+08, -3.61924940e+08, -3.47276865e+08, -5.76851498e+08]])
expected_disaggregated_households_round_erred = pd.DataFrame(expected_disaggregated_households_round_erred_data,
                                                             index=account_data_index,
                                                             columns=account_data_rate_columns)


def test_disaggregate_column():
    pd.testing.assert_frame_equal(hhd.disaggregate_column('Households',
                                                          account_data,
                                                          account_data_rate),
                                  expected_disaggregated_households_round_erred)


expected_disaggregated_households_data = np.array([[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [ 7.30525585e+06,  7.70556268e+06,  8.49460463e+06, 1.08796707e+07,  1.21954109e+07,  1.44937600e+07, 1.66607069e+07,  1.96268212e+07,  2.20888850e+07, 3.43936065e+07],
                                                   [ 8.18797580e+06,  2.27927145e+07,  3.07833320e+07, 4.44493791e+07,  5.45850175e+07,  7.04009393e+07, 8.28494671e+07,  9.97954737e+07,  1.12821255e+08, 2.13802167e+08],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [ 3.93418301e+06,  5.28169507e+06,  6.13007287e+06, 8.31928508e+06,  8.55138544e+06,  1.46545248e+07, 1.59109908e+07,  1.69810234e+07,  1.62937558e+07, 2.70650837e+07],
                                                   [ 3.08013684e+06,  4.57586372e+06,  4.99210918e+06, 4.42459558e+06,  4.50886836e+06,  3.68384088e+06, 3.91280596e+06,  3.94381734e+06,  4.28269167e+06, 5.14527046e+06],
                                                   [ 5.57093437e+06,  1.60289458e+07,  2.32573742e+07, 2.55551264e+07,  2.74006599e+07,  2.72045040e+07, 2.92423341e+07,  3.12223623e+07,  4.03325612e+07, 5.27281977e+07],
                                                   [ 1.99890197e+07,  1.95199397e+07,  1.33941267e+07, 9.72164412e+06,  7.79799840e+06,  6.72308026e+06, 5.71390565e+06,  5.07343982e+06,  3.58075951e+06, 2.73108618e+06],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [ 1.17856839e+06,  1.60916103e+06,  1.85408702e+06, 2.26284572e+06,  2.41688089e+06,  2.37832602e+06, 2.51159888e+06,  2.83869892e+06,  3.40608312e+06, 4.40001101e+06],
                                                   [-2.01329745e+05, -7.29283934e+05, -9.83001435e+05, -1.68821132e+06, -2.69082550e+06, -5.65705329e+06, -8.54890429e+06, -1.44637292e+07, -2.31838895e+07, -8.44877718e+07],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                   [-7.47054004e+05, -9.38818138e+05, -1.03559494e+06, -1.51692870e+06, -1.80724204e+06, -2.13827380e+06, -2.42190762e+06, -2.71880305e+06, -3.34852724e+06, -4.94485045e+06],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 1.29337627e+09],
                                                   [ 6.63570362e+07,  7.29401788e+07,  8.07391056e+07, 9.09907475e+07,  9.73074147e+07,  1.07256132e+08, 1.15977181e+08,  1.29219965e+08,  1.43448676e+08, 1.87093563e+08],
                                                   [ 4.60409679e+06,  5.54462904e+06,  2.82737183e+06, 3.06197609e+06,  6.79414552e+06,  1.10650563e+07, 1.03128780e+07,  2.02277050e+07,  2.23499109e+07, 2.55242305e+07],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 1.20364200e+09],
                                                   [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 8.97342660e+07],
                                                   [-8.38511858e+07, -1.12571376e+08, -1.30653271e+08, -1.77313032e+08, -1.82259902e+08, -3.12339125e+08, -3.39118806e+08, -3.61924940e+08, -3.47276865e+08, -5.76851498e+08]])
expected_disaggregated_households = pd.DataFrame(expected_disaggregated_households_data,
                                                 index=account_data_index,
                                                 columns=account_data_rate_columns)


def test_disaggregate_column_non_round_erred():
    pd.testing.assert_frame_equal(hhd.disaggregate_column_non_round_erred('Households',
                                                                          account_data,
                                                                          account_data_rate,
                                                                          'H10'),
                                  expected_disaggregated_households)


def test_normalize_error_in_disaggregation():
    pd.testing.assert_frame_equal(hhd.normalize_error_in_disaggregation(expected_disaggregated_households_round_erred,
                                                                        'H10',
                                                                        account_data.loc[:, 'Households']),
                                  expected_disaggregated_households)


def test_replace_disaggregated_column():
    expected_reindexed_account_data_data = np.array([[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 5.25107308e+07],
                                                     [ 4.06638882e+08,  5.78636011e+07,  7.30525585e+06, 7.70556268e+06,  8.49460463e+06,  1.08796707e+07, 1.21954109e+07,  1.44937600e+07,  1.66607069e+07, 1.96268212e+07,  2.20888850e+07,  3.43936064e+07, 0.00000000e+00],
                                                     [ 0.00000000e+00,  0.00000000e+00,  8.18797580e+06, 2.27927145e+07,  3.07833320e+07,  4.44493791e+07, 5.45850175e+07,  7.04009393e+07,  8.28494671e+07, 9.97954737e+07,  1.12821255e+08,  2.13802166e+08, 0.00000000e+00],
                                                     [ 0.00000000e+00,  3.25294206e+08,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [ 0.00000000e+00,  5.73055854e+07,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [ 0.00000000e+00,  2.35770000e+07,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [ 0.00000000e+00,  3.66130000e+07,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [ 0.00000000e+00,  1.35578990e+08,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [-6.88230000e+07, -3.13600000e+07,  3.93418301e+06, 5.28169507e+06,  6.13007287e+06,  8.31928508e+06, 8.55138544e+06,  1.46545248e+07,  1.59109908e+07, 1.69810234e+07,  1.62937558e+07,  2.70650837e+07, -2.29390000e+07],
                                                     [ 0.00000000e+00, -4.25500000e+07,  3.08013684e+06, 4.57586372e+06,  4.99210918e+06,  4.42459558e+06, 4.50886836e+06,  3.68384088e+06,  3.91280596e+06, 3.94381734e+06,  4.28269167e+06,  5.14527046e+06, 0.00000000e+00],
                                                     [ 0.00000000e+00, -2.78543000e+08,  5.57093437e+06, 1.60289458e+07,  2.32573742e+07,  2.55551264e+07, 2.74006599e+07,  2.72045040e+07,  2.92423341e+07, 3.12223623e+07,  4.03325612e+07,  5.27281977e+07, 0.00000000e+00],
                                                     [ 0.00000000e+00, -9.42450000e+07,  1.99890197e+07, 1.95199397e+07,  1.33941267e+07,  9.72164412e+06, 7.79799840e+06,  6.72308026e+06,  5.71390565e+06, 5.07343982e+06,  3.58075951e+06,  2.73108618e+06, 0.00000000e+00],
                                                     [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [-9.05024286e+07,  5.80836174e+07,  1.17856839e+06, 1.60916103e+06,  1.85408702e+06,  2.26284572e+06, 2.41688089e+06,  2.37832602e+06,  2.51159888e+06, 2.83869892e+06,  3.40608312e+06,  4.40001101e+06, 7.56255024e+06],
                                                     [ 0.00000000e+00,  1.42634000e+08, -2.01329745e+05, -7.29283934e+05, -9.83001435e+05, -1.68821132e+06, -2.69082550e+06, -5.65705329e+06, -8.54890429e+06, -1.44637292e+07, -2.31838895e+07, -8.44877719e+07, 0.00000000e+00],
                                                     [-3.66830000e+07,  3.66830000e+07,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [ 0.00000000e+00,  2.16180000e+07, -7.47054004e+05, -9.38818138e+05, -1.03559494e+06, -1.51692870e+06, -1.80724204e+06, -2.13827380e+06, -2.42190762e+06, -2.71880305e+06, -3.34852724e+06, -4.94485045e+06, 0.00000000e+00],
                                                     [ 2.10630453e+08,  4.48553000e+08,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 3.71342810e+07],
                                                     [ 0.00000000e+00,  5.21643000e+08,  6.63570362e+07, 7.29401788e+07,  8.07391056e+07,  9.09907475e+07, 9.73074147e+07,  1.07256132e+08,  1.15977181e+08, 1.29219965e+08,  1.43448676e+08,  1.87093562e+08, 0.00000000e+00],
                                                     [ 2.00125000e+08,  6.42840000e+07,  4.60409679e+06, 5.54462904e+06,  2.82737183e+06,  3.06197609e+06, 6.79414552e+06,  1.10650563e+07,  1.03128780e+07, 2.02277050e+07,  2.23499109e+07,  2.55242304e+07, 0.00000000e+00],
                                                     [ 2.00125000e+08,  5.85927000e+08,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00],
                                                     [ 1.05054530e+07, -1.37374000e+08,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 3.71342810e+07],
                                                     [ 1.91128800e+09,  1.06758400e+09, -8.38511858e+07, -1.12571376e+08, -1.30653271e+08, -1.77313032e+08, -1.82259902e+08, -3.12339125e+08, -3.39118806e+08, -3.61924940e+08, -3.47276865e+08, -5.76851498e+08, -3.54712000e+08]])
    expected_reindexed_account_data_table = pd.DataFrame(expected_reindexed_account_data_data,
                                                         index=expected_disagggregated_account_table_index,
                                                         columns=expected_disagggregated_account_table_columns)
    pd.testing.assert_frame_equal(hhd.replace_disaggregated_column('Households',
                                                                   account_data,
                                                                   expected_disaggregated_households_round_erred),
                                  expected_reindexed_account_data_table)


def test_get_disaggregated_header():
    assert hhd.get_disaggregated_header('Households',
                                        pd.Index(account_data_columns),
                                        pd.Index(account_data_rate_columns)) == expected_disagggregated_account_table_columns


def test_update_row():
    data = np.arange(12.).reshape(3, 4)
    index = ['x', 'y', 'z']
    columns = ['a', 'b', 'c', 'd']
    df = pd.DataFrame(data,
                      index=index,
                      columns=columns)
    update_data = np.arange(40., 80., 10.)
    update_series = pd.Series(update_data,
                              index=columns)
    expected_data = np.array([[ 0.,  1.,  2.,  3.],
                              [40., 50., 60., 70.],
                              [ 8.,  9., 10., 11.]])
    expected_df = pd.DataFrame(expected_data,
                               index=index,
                               columns=columns)
    hhd.update_row('y', df, update_series)
    pd.testing.assert_frame_equal(df, expected_df)

