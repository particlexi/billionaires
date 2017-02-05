#analyze medicare part d prescription drug coverage

import pandas as pd

medfile = pd.read_table("PartD_Prescriber_PUF_NPI_14.txt")

#medfile["BENE_COUNT"].fillna(0,inplace=True)
#num_row = medfile.loc[medfile.BENE_COUNT>0,"BENE_COUNT"].count()
#sum_row = medfile.loc[medfile.BENE_COUNT>0,"BENE_COUNT"].sum()
#av = sum_row/num_row
#print '{:.9f}'.format(av)


#total_day_supply = medfile.loc[medfile.TOTAL_DAY_SUPPLY!=0,"TOTAL_DAY_SUPPLY"]
#total_claim_count = medfile.loc[medfile.TOTAL_CLAIM_COUNT!=0,"TOTAL_CLAIM_COUNT"]
#av_count = total_day_supply/total_claim_count
#median_count = av_count.median()
#print median_count


#medfile = medfile[medfile.TOTAL_CLAIM_COUNT>1000]
#medfile = medfile[(medfile.BRAND_SUPPRESS_FLAG!="*") & (medfile.BRAND_SUPPRESS_FLAG!="#")]
#total_claim_spec = medfile.groupby("SPECIALTY_DESCRIPTION")["TOTAL_CLAIM_COUNT"].sum()
#brand_claim_drug = medfile.groupby("SPECIALTY_DESCRIPTION")["BRAND_CLAIM_COUNT"].sum()
#ratio_brand = brand_claim_drug/total_claim_spec
#print '{:.9f}'.format(ratio_brand.std())


#medfile = medfile[medfile.TOTAL_CLAIM_COUNT>1000]
#medfile = medfile[(medfile.BRAND_SUPPRESS_FLAG!="*") & (medfile.BRAND_SUPPRESS_FLAG!="#")]
#opioid_state = medfile.groupby("NPPES_PROVIDER_STATE")["OPIOID_BENE_COUNT"].sum()
#antibiotic_state = medfile.groupby("NPPES_PROVIDER_STATE")["ANTIBIOTIC_BENE_COUNT"].sum()
#ratio_on = opioid_state/antibiotic_state
#print '{:.9f}'.format(ratio_on.max()-ratio_on.min())


#medfile["BENE_COUNT"].fillna(0,inplace=True)
#medfile = medfile[medfile.BENE_COUNT>0]
#medfile = medfile[(medfile.GE65_SUPPRESS_FLAG!="*") & (medfile.GE65_SUPPRESS_FLAG!="#")]
#medfile = medfile[(medfile.LIS_SUPPRESS_FLAG!="*") & (medfile.LIS_SUPPRESS_FLAG!="#")]
#ratio_over65 = medfile["TOTAL_CLAIM_COUNT_GE65"]/medfile["TOTAL_CLAIM_COUNT"]
#ratio_lis = medfile["LIS_CLAIM_COUNT"]/medfile["TOTAL_CLAIM_COUNT"]
##pearson_cor = ratio_over65.corr(ratio_lis)
#pearson_cor = ratio_lis.corr(ratio_over65)
#print '{:.9f}'.format(pearson_cor)


#n_provider = medfile["NPI"].count()
#medfile["AVE_OPIOID"] = medfile["OPIOID_DAY_SUPPLY"]/medfile["OPIOID_CLAIM_COUNT"]
#medfile.AVE_OPIOID.fillna(0,inplace=True)
#state_spec_count = medfile.groupby(["SPECIALTY_DESCRIPTION","NPPES_PROVIDER_STATE"])["NPI"].count()>100
#opioid_state_spec = medfile.groupby(["SPECIALTY_DESCRIPTION","NPPES_PROVIDER_STATE"])["AVE_OPIOID"].sum()
#opioid_state_spec = opioid_state_spec[state_spec_count==True]/n_provider
#opioid_state_spec = opioid_state_spec.to_frame()
#state_opioid_spec = opioid_state_spec.unstack()
#state_opioid_spec.fillna(0,inplace=True)
#opioid_spec = medfile.groupby(["SPECIALTY_DESCRIPTION"])["AVE_OPIOID"].sum()
#opioid_spec = opioid_spec/n_provider
#sel_opioid_spec = opioid_spec[opioid_spec.index.intersection(state_opioid_spec.index)]
#ratio_sel = state_opioid_spec.div(sel_opioid_spec,axis='index')
#max_ratio = ratio_sel.max().max()
#print '{:.9f}'.format(max_ratio) 


##########################################################################################
medfile13 = pd.read_table("PARTD_PRESCRIBER_PUF_NPI_13.tab")

#medfile13["TOTAL_DAY_SUPPLY"].fillna(0,inplace=True)
#medfile13["TOTAL_DRUG_COST"].fillna(0,inplace=True)
#amedfile13 = medfile13[(medfile13.TOTAL_DAY_SUPPLY>0) & (medfile13.TOTAL_DRUG_COST>0)]
#av_cost13 = amedfile13["TOTAL_DRUG_COST"]/amedfile13["TOTAL_DAY_SUPPLY"]
#av_cost13 = pd.concat([medfile13["NPI"],av_cost13],axis=1)
#av_cost13.columns = ["npi","avcost"]
#del amedfile13
#medfile["TOTAL_DAY_SUPPLY"].fillna(0,inplace=True)
#medfile["TOTAL_DRUG_COST"].fillna(0,inplace=True)
#amedfile = medfile[(medfile.TOTAL_DAY_SUPPLY>0) & (medfile.TOTAL_DRUG_COST>0)]
#av_cost14 = amedfile["TOTAL_DRUG_COST"]/amedfile["TOTAL_DAY_SUPPLY"]
#av_cost14 = pd.concat([medfile["NPI"],av_cost14],axis=1)
#av_cost14.columns = ["npi","avcost"]
#del amedfile
#av_cost = pd.merge(av_cost13,av_cost14,on=["npi"],how="inner")
#inflation = (av_cost["avcost_y"]-av_cost["avcost_x"])/av_cost["avcost_x"]
#av_inflation = inflation.mean()
#print '{:.9f}'.format(av_inflation) 

medfile["SPECIALTY_DESCRIPTION"].fillna(0,inplace=True)
medfile = medfile[(medfile.SPECIALTY_DESCRIPTION!=0)]
medfile13["SPECIALTY_DESC"].fillna(0,inplace=True)
medfile13 = medfile13[(medfile13.SPECIALTY_DESC!=0)]
npi_spec13 = pd.concat([medfile13["NPI"],medfile13["SPECIALTY_DESC"]],axis=1)
npi_spec13.columns = ["npi","spec"]
npi_spec14 = pd.concat([medfile["NPI"],medfile["SPECIALTY_DESCRIPTION"]],axis=1)
npi_spec14.columns = ["npi","spec"]
npi_spec = pd.merge(npi_spec13,npi_spec14,on=["npi"],how="inner")
left_spec = abs((npi_spec["spec_x"]==npi_spec["spec_y"]).astype(int)-1)
npi_left = pd.concat([npi_spec,left_spec],axis=1)
npi_left.columns = ["npi","spec13","spec14","left"]
left_cnt_flg = npi_left.groupby(["spec13"])["left"].count()>1000
left_cnt = npi_left.groupby(["spec13"])["left"].count()
left_sum = npi_left.groupby(["spec13"])["left"].sum()
ratio_left = left_sum[left_cnt_flg==True]/left_cnt[left_cnt_flg==True]
print '{:.9f}'.format(ratio_left.max()) 