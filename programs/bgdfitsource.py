#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:47:25 2019

@author: jpadial
"""
import numpy
from sherpa.astro.ui import *

#### user input ####

indir_1 = input('input directory data 1:')
indir_2 = input('input directory data 2:')

module_1 = input('Focal plane data 1- ¿A or B?:')
module_2 = input('Focal plane data 2- ¿A or B?:')

region_1 = input('region 1- ¿A,B,C?:')
region_2 = input('region 2- ¿A,B,C?:')

obs_1 = input('obsid data 1- ¿002 or 004?:')
obs_2 = input('obsid data 2- ¿002 or 004?:')


# variables from user input #

## RMF FILES ##

RMF_1 = indir_1 +'src/'+'reg'+region_1+'_'+ obs_1+module_1 +'_sr.rmf' 

RMF_2 = indir_2 +'src/'+ 'reg'+region_2+'_'+ obs_2+module_2 +'_sr.rmf'

## FIT Components ##

### aperture background ###

apbgd_1 = indir_1 +'src/'+ 'bgdapreg'+region_1+'_'+ obs_1+module_1 +'_sr.pha'

apbgd_2 = indir_2 +'src/'+ 'bgdapreg'+region_2+'_'+ obs_2+module_2 +'_sr.pha'


### fcxb ###


fcxb_1 = indir_1 +'src/'+ 'bgdfcxbreg'+region_1+'_'+ obs_1+module_1 +'_sr.pha'

fcxb_2 = indir_2 +'src/'+'bgdfcxbreg'+region_2+'_'+ obs_2+module_2 +'_sr.pha'

### Instrument components # ##

instr_1 = indir_1 +'src/'+'bgdinstrreg'+region_1+'_'+obs_1+module_1+'_sr.pha'

instr_2 = indir_2 +'src/'+'bgdinstrreg'+region_2+'_'+obs_2+module_2+'_sr.pha'

### internal contiuum ###

contin_2 = indir_2 +'src/'+'bgdintcontreg'+region_2+'_'+obs_2+module_2+'_sr.pha'

contin_1 = indir_1 +'src/'+'bgdintcontreg'+region_1+'_'+obs_1+module_1+'_sr.pha'

### fit ###

fit_1 = indir_1 +'src/'+'bgd_allint_reg'+region_1+'_'+obs_1+module_1+'_sr.pha'
fit_2 = indir_2 +'src/'+'bgd_allint_reg'+region_2+'_'+obs_2+module_2+'_sr.pha'

### bgd ###

bgd_1 = indir_1+'src/' +'bgdreg'+region_1+'_'+obs_1+module_1+'_sr.pha'
bgd_2 = indir_2+'src/' +'bgdreg'+region_2+'_'+obs_2+module_2+'_sr.pha'


### source ###


source_1 = indir_1+'src/' +'reg'+region_1+'_'+obs_1+module_1+'_sr.pha'
source_2 = indir_2 +'src/'+'reg'+region_2+'_'+obs_2+module_2+'_sr.pha'

###  extraction ###

extract_1 = indir_1+'bgdspec/'+'bgd1'+module_1+'_sr.pha'

extract_2 = indir_2+'bgdspec/'+'bgd1'+module_2+'_sr.pha'


#################################################

# load data 1

load_data(1,apbgd_1)
load_rmf(1,RMF_1)
set_analysis(1,"ener")
notice_id(1, 3.0,155.0)
group_counts(1,30)

load_data(2,fcxb_1)
load_rmf(2,RMF_1)
set_analysis(2,"ener")
notice_id(2, 3.0, 155.0)
group_counts(2,30)

load_data(3,instr_1)
load_rmf(3,RMF_1)
set_analysis(3,"ener")
notice_id(3, 3.0, 155.0)
group_counts(3,30)


load_data(4,contin_1)
load_rmf(4,RMF_1)
set_analysis(4,"ener")
notice_id(4, 3.0, 155.0)
group_counts(4,30)

load_data(5,fit_1)
load_rmf(5,RMF_1)
set_analysis(5,"ener")
notice_id(5, 3.0, 155.0)
group_counts(5,30)

load_data(6,bgd_1)
load_rmf(6,RMF_1)
set_analysis(6,"ener")
notice_id(6, 3.0, 155.0)
group_counts(6,30)

# load data 2

load_data(7,apbgd_2)
load_rmf(7,RMF_2)
set_analysis(7,"ener")
notice_id(7, 3.0, 155.0)
group_counts(7,30)

load_data(8,fcxb_2)
load_rmf(8,RMF_2)
set_analysis(8,"ener")
notice_id(8, 3.0, 155.0)
group_counts(8,30)

load_data(9,instr_2)
load_rmf(9,RMF_2)
set_analysis(9,"ener")
notice_id(9, 3.0, 155.0)
group_counts(9,30)


load_data(10,contin_2)
load_rmf(10,RMF_2)
set_analysis(10,"ener")
notice_id(10, 3.0, 155.0)
group_counts(10,30)

load_data(11,fit_2)
load_rmf(11,RMF_2)
set_analysis(11,"ener")
notice_id(11, 3.0, 155.0)
group_counts(11,30)

load_data(12,bgd_2)
load_rmf(12,RMF_2)
set_analysis(12,"ener")
notice_id(12, 3.0, 155.0)
group_counts(12,30)


####### load source

load_data(13,source_1)
load_rmf(13,RMF_1)
set_analysis(13,"ener")
notice_id(13, 3.0, 155.0)
group_counts(13,30)


load_data(14,source_2)
load_rmf(14,RMF_2)
set_analysis(14,"ener")
notice_id(14, 3.0, 155.0)
group_counts(14,30)


###### load bgd extraction ####

load_data(15,extract_1)
load_rmf(15,RMF_1) 
set_analysis(15,"ener")
notice_id(15, 3.0, 155.0)
group_counts(15,30)


load_data(16,extract_2)
load_rmf(16,RMF_2) 
set_analysis(16,"ener")
notice_id(16, 3.0, 155.0)
group_counts(16,30)



############# start plot

set_xlog()
set_ylog()
  

plot_data(1)
plot_data(2,overplot=True)
plot_data(3,overplot=True)
plot_data(4,overplot=True)
plot_data(5,overplot=True)
plot_data(6,overplot=True)
plot_data(7,overplot=True)
plot_data(8,overplot=True)
plot_data(9,overplot=True)
plot_data(10,overplot=True)
plot_data(11,overplot=True)
plot_data(12,overplot=True)
plot_data(13,overplot=True)
plot_data(14,overplot=True)
plot_data(15,overplot=True)
plot_data(16,overplot=True)



set_curve("crv1",["*.color","green","symbol.style","circle","err.*","false"])   #apbgd
set_curve("crv2",["*.color","orange","symbol.style","circle","err.*","false"])  #fcxb
set_curve("crv3",["*.color","cyan","symbol.style","circle","err.*","false"])   #instr
set_curve("crv4",["*.color","magenta","symbol.style","circle","err.*","false"])  # int cont
set_curve("crv5",["*.color","blue","symbol.style","circle","err.*","false"]) # all 
set_curve("crv6",["*.color","red"])  # data

set_curve("crv7",["*.color","green","symbol.style","uptriangle","err.*","false"])  #apbgd
set_curve("crv8",["*.color","orange","symbol.style","uptriangle","err.*","false"]) #fcxb
set_curve("crv9",["*.color","cyan","symbol.style","uptriangle","err.*","false"])  #instr
set_curve("crv10",["*.color","magenta","symbol.style","uptriangle","err.*","false"]) # int cont
set_curve("crv11",["*.color","yellow","symbol.style","uptriangle","err.*","false"]) # all 
set_curve("crv12",["*.color","red","symbol.style","uptriangle"]) #data
set_curve("crv14",["symbol.style","uptriangle"])
set_curve("crv15",["symbol.style","circle","*.color","maroon"])
set_curve("crv16",["symbol.style","uptriangle","*.color","maroon"])

#limits(Y_AXIS, 1e-05,0.01)

fit_data1 = 'reg'+region_1+'fit-'+obs_1+module_1
fit_data2 = 'reg'+region_2+'fit-'+obs_2+module_2



add_label(65,6e-02,'apgbgd')
add_label(106,6e-02,'fcxb')
add_label(65,3e-02,'instr')
add_label(106,3e-02,'int cont')
add_label(65,2e-02,fit_data1)
add_label(106,2e-02,fit_data2)
add_label(65,1.5e-02,'bgd')
add_label(106,1.5e-02,'source')
add_label(65,1.0e-02,'bgd extraction')

set_label("lbl1",["*.color","green"])
set_label("lbl2",["*.color","orange"])
set_label("lbl3",["*.color","cyan"])
set_label("lbl4",["*.color","magenta"])
set_label("lbl5",["*.color","blue"])
set_label("lbl6",["*.color","yellow"])
set_label("lbl7",["*.color","red"])
set_label("lbl9",["*.color","maroon"])

plot_title= 'circle=reg'+region_1+indir_1+'FPM'+module_1+'&'+'triangle=reg'+region_2+indir_2+'FPM'+module_2
set_plot_title(plot_title)
  
limits(Y_AXIS,1e-06,1e-01)

