export SAS_CCF=~/Desktop/research/XMM/0110012501/MOS1/ccf.cif
export SAS_ODF=~/Desktop/research/XMM/0110012501/MOS1/0592_0110012501_SCX00000SUM.SAS

evselect table=~/Desktop/research/XMM/0110012501/MOS1/S2501_MOS1_filt_time.fits imageset=~/Desktop/research/XMM/data_for_mosaic/S2501_MOS1_4keV_7500eV_image.fits withimageset=yes imagebinning=binSize xcolumn=X ycolumn=Y ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM && (PI in [4000:7500]) && (PATTERN in [0:12]) && (FLAG==0)' 


evselect table=~/Desktop/research/XMM/0110012501/MOS2/S2501_MOS2_filt_time.fits imageset=~/Desktop/research/XMM/data_for_mosaic/S2501_MOS2_4keV_7500eV_image.fits withimageset=yes imagebinning=binSize xcolumn=X ycolumn=Y ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EM && (PI in [4000:7500]) && (PATTERN in [0:12]) && (FLAG==0)' 


evselect table=~/Desktop/research/XMM/0110012501/PN/U2501_PN_filt_time.fits imageset=~/Desktop/research/XMM/data_for_mosaic/U2501_PN_4keV_7500eV_image.fits withimageset=yes imagebinning=binSize xcolumn=X ycolumn=Y ximagebinsize=40 yimagebinsize=40 expression='#XMMEA_EP && (PI in [4000:7500]) && (PATTERN in [0:4]) && (FLAG==0)' 


eexpmap imageset=~/Desktop/research/XMM/data_for_mosaic/S2501_MOS1_4keV_7500eV_image.fits eventset=~/Desktop/research/XMM/0110012501/MOS1/S2501_MOS1_filt_time.fits expimageset=~/Desktop/research/XMM/data_for_mosaic/S2501_MOS1_4kev_7500eV_exp.fits attitudeset=~/Desktop/research/XMM/0110012501/MOS1/attitude.fits pimin='4000' pimax='7500' withvignetting=yes &

eexpmap imageset=~/Desktop/research/XMM/data_for_mosaic/S2501_MOS2_4keV_7500eV_image.fits eventset=~/Desktop/research/XMM/0110012501/MOS2/S2501_MOS2_filt_time.fits expimageset=~/Desktop/research/XMM/data_for_mosaic/S2501_MOS2_4kev_7500eV_exp.fits attitudeset=~/Desktop/research/XMM/0110012501/MOS2/attitude.fits pimin='4000' pimax='7500' withvignetting=yes &


eexpmap imageset=~/Desktop/research/XMM/data_for_mosaic/U2501_PN_4keV_7500eV_image.fits eventset=~/Desktop/research/XMM/0110012501/PN/U2501_PN_filt_time.fits expimageset=~/Desktop/research/XMM/data_for_mosaic/U2501_PN_4kev_7500eV_exp.fits attitudeset=~/Desktop/research/XMM/0110012501/PN/attitude.fits pimin='4000' pimax='7500' withvignetting=yes &

wait







