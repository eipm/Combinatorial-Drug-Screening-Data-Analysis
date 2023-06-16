## ---- include = FALSE---------------------------------------------------------
knitr::opts_chunk$set(
  collapse = TRUE,
  comment = "#>"
)

# ## ----eval=FALSE---------------------------------------------------------------
 if (!requireNamespace("BiocManager", quietly = TRUE))
   install.packages("BiocManager")
 
 BiocManager::install("synergyfinder")
install.packages("readxl")
library(readxl)

## ----message=FALSE------------------------------------------------------------
library(synergyfinder)

example_file <- file.choose("C:/Users/oma4008/OneDrive - med.cornell.edu/Documents/Manish.PM1352.DRC.PLATES.082322.csv")
data <- read_excel(example_file)

## -----------------------------------------------------------------------------
res <- ReshapeData(
  data = data,
  data_type = "viability",
  impute = TRUE,
  impute_method = NULL,
  noise = TRUE,
  seed = 1)

## -----------------------------------------------------------------------------
str(res)

## ----message=FALSE, warning=FALSE---------------------------------------------
res <- CalculateSynergy(
  data = res,
  method = c("ZIP", "HSA", "Bliss", "Loewe"),
  Emin = NA,
  Emax = NA,
  correct_baseline = "non")

## -----------------------------------------------------------------------------
res$drug_pairs
str(res$synergy_scores)

## ----fig.cap="Figure 1. Concept of RI", fig.show="hold", out.width="60%"------
knitr::include_graphics("C:/Users/oma4008/AppData/Local/R/win-library/4.3/knitr")

## ----message=FALSE, warning=FALSE---------------------------------------------
res <- CalculateSensitivity(
  data = res,
  correct_baseline = "non"
)

## -----------------------------------------------------------------------------
sensitive_columns <- c(
  "block_id", "drug1", "drug2",
  "ic50_1", "ic50_2",
  "ri_1", "ri_2",
  "css1_ic502", "css2_ic501", "css")
res$drug_pairs[, sensitive_columns]

## ----message=FALSE, warning=FALSE, fig.width=7, fig.height=4, out.width="100%"----
for (i in c(1, 2)){
  PlotDoseResponseCurve(
    data = res,
    plot_block = 1,
    drug_index = i,
    plot_new = FALSE,
    record_plot = FALSE
  )
}

## ----fig.show="hold", fig.width=7, fig.height=4, out.width="100%"-------------
Plot2DrugHeatmap(
    data = res,
    plot_block = 1,
    drugs = c(1, 2),
    plot_value = "response",
    dynamic = FALSE,
    summary_statistic = c("mean",  "median")
  )

Plot2DrugHeatmap(
    data = res,
    plot_block = 1,
    drugs = c(1, 2),
    plot_value = "ZIP_synergy",
    dynamic = FALSE,
    summary_statistic = c( "quantile_25", "quantile_75")
  )

## ----fig.show="hold", fig.width=7, fig.height=4, out.width="100%"-------------
Plot2DrugContour(
    data = res,
    plot_block = 1,
    drugs = c(1, 2),
    plot_value = "response",
    dynamic = FALSE,
    summary_statistic = c("mean", "median")
  )
Plot2DrugContour(
    data = res,
    plot_block = 1,
    drugs = c(1, 2),
    plot_value = "ZIP_synergy",
    dynamic = FALSE,
    summary_statistic = c("quantile_25", "quantile_75")
  )

## ----fig.width=9, fig.height=6, eval=FALSE------------------------------------
  Plot2DrugSurface(
    data = res,
    plot_block = 1,
    drugs = c(1, 2),
    plot_value = "response",
    dynamic = FALSE,
    summary_statistic = c("mean", "quantile_25", "median", "quantile_75")
  )
  Plot2DrugSurface(
    data = res,
    plot_block = 1,
    drugs = c(1, 2),
    plot_value = "ZIP_synergy",
    dynamic = FALSE,
    summary_statistic = c("mean", "quantile_25", "median", "quantile_75")
  )

## ----fig.width=6, fig.height=4, fig.show="hold", out.width="100%", echo=FALSE----
for (v in c("response", "ZIP_synergy")) {
  Plot2DrugSurface(
    data = res,
    plot_block = 1,
    drugs = c(1, 2),
    plot_value = v,
    dynamic = FALSE,
    summary_statistic = c("mean", "quantile_25", "median", "quantile_75")
  )
}

## ----fig.width=6, fig.height=4, eval=FALSE------------------------------------
  PlotDoseResponse(
    data = res,
    block_ids = c(1, 2),
    drugs = c(1,2),
    save_file = TRUE,
    file_type = "png"
  )

## ----fig.width=6, fig.height=4, fig.show="hold", out.width="100%", echo=FALSE----
#knitr::include_graphics("./ispinesib_ibrutinib_adjusted_dose_response_block_1.png")
#knitr::include_graphics("./canertinib_ibrutinib_adjusted_dose_response_block_2.png")
  knitr::include_graphics("C:/Users/oma4008/AppData/Local/R/win-library/4.3/knitr")
  
## ----fig.width=6, fig.height=4, eval=FALSE------------------------------------
  PlotSynergy(
    data = res,
    type = "2D",
    method = "ZIP",
    block_ids = c(1, 2),
    drugs = c(1,2),
    save_file = TRUE,
    file_type = "png"
  )

## ----fig.width=6, fig.height=4, fig.show="hold", out.width="100%", echo=FALSE----
#knitr::include_graphics("./ispinesib_ibrutinib_synergy_1_ZIP_2D.png")
#knitr::include_graphics("./canertinib_ibrutinib_synergy_2_ZIP_2D.png")
  knitr::include_graphics("C:/Users/oma4008/AppData/Local/R/win-library/4.3/knitr")

## ----fig.width=6, fig.height=4, fig.show="hold", out.width="100%"-------------
# Block1: ispinesib (drug1) 9.7656 nM + ibrutinib (drug2) 50 nM
PlotBarometer(
  data = res,
  plot_block = 1,
  plot_concs = c(0, 10), 
  needle_text_offset = 2.5 # Move the texts below the needle
)
# Block2: Canertinib (drug1) 625 nM + Ibrutinib (drug2) 12.5 nM
#PlotBarometer(
#  data = res, 
#  plot_block = 2, 
#  plot_concs = c(10, 10),
#  needle_text_offset = -2.5 # Move the texts above the needle
#)


## ----fig.width=12, fig.height=9, fig.show="hold", out.width="100%"------------
#PlotMultiDrugBar(
 # data = res,
 # plot_block = 1,
 # plot_value = c("response", "ZIP_synergy", "Loewe_synergy", "HSA_synergy", "Bliss_synergy"),
 # sort_by = "response",
 # highlight_row = c(9.7656, 50),
 # highlight_label_size = 8
#)

## -----------------------------------------------------------------------------
PlotSensitivitySynergy(
  data = res,
  plot_synergy = "ZIP",
  show_labels = TRUE,
  dynamic = FALSE
)

