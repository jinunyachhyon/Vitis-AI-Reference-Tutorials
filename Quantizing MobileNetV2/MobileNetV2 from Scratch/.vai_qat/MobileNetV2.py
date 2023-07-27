# GENETARED BY NNDCT, DO NOT EDIT!

import torch
from torch import tensor
import pytorch_nndct as py_nndct

class MobileNetV2(py_nndct.nn.NndctQuantModel):
    def __init__(self):
        super(MobileNetV2, self).__init__()
        self.module_0 = py_nndct.nn.Input() #MobileNetV2::input_0(MobileNetV2::nndct_input_0)
        self.module_1 = py_nndct.nn.quant_input() #MobileNetV2::MobileNetV2/QuantStub[quant_stub]/10394(MobileNetV2::nndct_quant_stub_1)
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/Sequential[0]/Conv2d[0]/ret.5(MobileNetV2::nndct_conv2d_2)
        self.module_3 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/Sequential[0]/ReLU6[2]/10427(MobileNetV2::nndct_relu6_3)
        self.module_4 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[1]/Sequential[conv]/Conv2d[0]/ret.9(MobileNetV2::nndct_depthwise_conv2d_4)
        self.module_5 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[1]/Sequential[conv]/ReLU6[2]/10457(MobileNetV2::nndct_relu6_5)
        self.module_6 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[1]/Sequential[conv]/Conv2d[3]/ret.13(MobileNetV2::nndct_conv2d_6)
        self.module_7 = py_nndct.nn.Conv2d(in_channels=16, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/Conv2d[0]/ret.17(MobileNetV2::nndct_conv2d_7)
        self.module_8 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/ReLU6[2]/10514(MobileNetV2::nndct_relu6_8)
        self.module_9 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=96, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/Conv2d[3]/ret.21(MobileNetV2::nndct_depthwise_conv2d_9)
        self.module_10 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/ReLU6[5]/10544(MobileNetV2::nndct_relu6_10)
        self.module_11 = py_nndct.nn.Conv2d(in_channels=96, out_channels=24, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[2]/Sequential[conv]/Conv2d[6]/ret.25(MobileNetV2::nndct_conv2d_11)
        self.module_12 = py_nndct.nn.Conv2d(in_channels=24, out_channels=144, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/Conv2d[0]/ret.29(MobileNetV2::nndct_conv2d_12)
        self.module_13 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/ReLU6[2]/10601(MobileNetV2::nndct_relu6_13)
        self.module_14 = py_nndct.nn.Conv2d(in_channels=144, out_channels=144, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=144, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/Conv2d[3]/ret.33(MobileNetV2::nndct_depthwise_conv2d_14)
        self.module_15 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/ReLU6[5]/10631(MobileNetV2::nndct_relu6_15)
        self.module_16 = py_nndct.nn.Conv2d(in_channels=144, out_channels=24, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Sequential[conv]/Conv2d[6]/ret.37(MobileNetV2::nndct_conv2d_16)
        self.module_17 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[3]/Add[skip_add]/ret.41(MobileNetV2::nndct_elemwise_add_17)
        self.module_18 = py_nndct.nn.Conv2d(in_channels=24, out_channels=144, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/Conv2d[0]/ret.43(MobileNetV2::nndct_conv2d_18)
        self.module_19 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/ReLU6[2]/10691(MobileNetV2::nndct_relu6_19)
        self.module_20 = py_nndct.nn.Conv2d(in_channels=144, out_channels=144, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=144, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/Conv2d[3]/ret.47(MobileNetV2::nndct_depthwise_conv2d_20)
        self.module_21 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/ReLU6[5]/10721(MobileNetV2::nndct_relu6_21)
        self.module_22 = py_nndct.nn.Conv2d(in_channels=144, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[4]/Sequential[conv]/Conv2d[6]/ret.51(MobileNetV2::nndct_conv2d_22)
        self.module_23 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/Conv2d[0]/ret.55(MobileNetV2::nndct_conv2d_23)
        self.module_24 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/ReLU6[2]/10778(MobileNetV2::nndct_relu6_24)
        self.module_25 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/Conv2d[3]/ret.59(MobileNetV2::nndct_depthwise_conv2d_25)
        self.module_26 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/ReLU6[5]/10808(MobileNetV2::nndct_relu6_26)
        self.module_27 = py_nndct.nn.Conv2d(in_channels=192, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Sequential[conv]/Conv2d[6]/ret.63(MobileNetV2::nndct_conv2d_27)
        self.module_28 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[5]/Add[skip_add]/ret.67(MobileNetV2::nndct_elemwise_add_28)
        self.module_29 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/Conv2d[0]/ret.69(MobileNetV2::nndct_conv2d_29)
        self.module_30 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/ReLU6[2]/10868(MobileNetV2::nndct_relu6_30)
        self.module_31 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/Conv2d[3]/ret.73(MobileNetV2::nndct_depthwise_conv2d_31)
        self.module_32 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/ReLU6[5]/10898(MobileNetV2::nndct_relu6_32)
        self.module_33 = py_nndct.nn.Conv2d(in_channels=192, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Sequential[conv]/Conv2d[6]/ret.77(MobileNetV2::nndct_conv2d_33)
        self.module_34 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[6]/Add[skip_add]/ret.81(MobileNetV2::nndct_elemwise_add_34)
        self.module_35 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/Conv2d[0]/ret.83(MobileNetV2::nndct_conv2d_35)
        self.module_36 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/ReLU6[2]/10958(MobileNetV2::nndct_relu6_36)
        self.module_37 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/Conv2d[3]/ret.87(MobileNetV2::nndct_depthwise_conv2d_37)
        self.module_38 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/ReLU6[5]/10988(MobileNetV2::nndct_relu6_38)
        self.module_39 = py_nndct.nn.Conv2d(in_channels=192, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[7]/Sequential[conv]/Conv2d[6]/ret.91(MobileNetV2::nndct_conv2d_39)
        self.module_40 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/Conv2d[0]/ret.95(MobileNetV2::nndct_conv2d_40)
        self.module_41 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/ReLU6[2]/11045(MobileNetV2::nndct_relu6_41)
        self.module_42 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/Conv2d[3]/ret.99(MobileNetV2::nndct_depthwise_conv2d_42)
        self.module_43 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/ReLU6[5]/11075(MobileNetV2::nndct_relu6_43)
        self.module_44 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Sequential[conv]/Conv2d[6]/ret.103(MobileNetV2::nndct_conv2d_44)
        self.module_45 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[8]/Add[skip_add]/ret.107(MobileNetV2::nndct_elemwise_add_45)
        self.module_46 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/Conv2d[0]/ret.109(MobileNetV2::nndct_conv2d_46)
        self.module_47 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/ReLU6[2]/11135(MobileNetV2::nndct_relu6_47)
        self.module_48 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/Conv2d[3]/ret.113(MobileNetV2::nndct_depthwise_conv2d_48)
        self.module_49 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/ReLU6[5]/11165(MobileNetV2::nndct_relu6_49)
        self.module_50 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Sequential[conv]/Conv2d[6]/ret.117(MobileNetV2::nndct_conv2d_50)
        self.module_51 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[9]/Add[skip_add]/ret.121(MobileNetV2::nndct_elemwise_add_51)
        self.module_52 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/Conv2d[0]/ret.123(MobileNetV2::nndct_conv2d_52)
        self.module_53 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/ReLU6[2]/11225(MobileNetV2::nndct_relu6_53)
        self.module_54 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/Conv2d[3]/ret.127(MobileNetV2::nndct_depthwise_conv2d_54)
        self.module_55 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/ReLU6[5]/11255(MobileNetV2::nndct_relu6_55)
        self.module_56 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Sequential[conv]/Conv2d[6]/ret.131(MobileNetV2::nndct_conv2d_56)
        self.module_57 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[10]/Add[skip_add]/ret.135(MobileNetV2::nndct_elemwise_add_57)
        self.module_58 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/Conv2d[0]/ret.137(MobileNetV2::nndct_conv2d_58)
        self.module_59 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/ReLU6[2]/11315(MobileNetV2::nndct_relu6_59)
        self.module_60 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/Conv2d[3]/ret.141(MobileNetV2::nndct_depthwise_conv2d_60)
        self.module_61 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/ReLU6[5]/11345(MobileNetV2::nndct_relu6_61)
        self.module_62 = py_nndct.nn.Conv2d(in_channels=384, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[11]/Sequential[conv]/Conv2d[6]/ret.145(MobileNetV2::nndct_conv2d_62)
        self.module_63 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/Conv2d[0]/ret.149(MobileNetV2::nndct_conv2d_63)
        self.module_64 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/ReLU6[2]/11402(MobileNetV2::nndct_relu6_64)
        self.module_65 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/Conv2d[3]/ret.153(MobileNetV2::nndct_depthwise_conv2d_65)
        self.module_66 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/ReLU6[5]/11432(MobileNetV2::nndct_relu6_66)
        self.module_67 = py_nndct.nn.Conv2d(in_channels=576, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Sequential[conv]/Conv2d[6]/ret.157(MobileNetV2::nndct_conv2d_67)
        self.module_68 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[12]/Add[skip_add]/ret.161(MobileNetV2::nndct_elemwise_add_68)
        self.module_69 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/Conv2d[0]/ret.163(MobileNetV2::nndct_conv2d_69)
        self.module_70 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/ReLU6[2]/11492(MobileNetV2::nndct_relu6_70)
        self.module_71 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/Conv2d[3]/ret.167(MobileNetV2::nndct_depthwise_conv2d_71)
        self.module_72 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/ReLU6[5]/11522(MobileNetV2::nndct_relu6_72)
        self.module_73 = py_nndct.nn.Conv2d(in_channels=576, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Sequential[conv]/Conv2d[6]/ret.171(MobileNetV2::nndct_conv2d_73)
        self.module_74 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[13]/Add[skip_add]/ret.175(MobileNetV2::nndct_elemwise_add_74)
        self.module_75 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/Conv2d[0]/ret.177(MobileNetV2::nndct_conv2d_75)
        self.module_76 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/ReLU6[2]/11582(MobileNetV2::nndct_relu6_76)
        self.module_77 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/Conv2d[3]/ret.181(MobileNetV2::nndct_depthwise_conv2d_77)
        self.module_78 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/ReLU6[5]/11612(MobileNetV2::nndct_relu6_78)
        self.module_79 = py_nndct.nn.Conv2d(in_channels=576, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[14]/Sequential[conv]/Conv2d[6]/ret.185(MobileNetV2::nndct_conv2d_79)
        self.module_80 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/Conv2d[0]/ret.189(MobileNetV2::nndct_conv2d_80)
        self.module_81 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/ReLU6[2]/11669(MobileNetV2::nndct_relu6_81)
        self.module_82 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/Conv2d[3]/ret.193(MobileNetV2::nndct_depthwise_conv2d_82)
        self.module_83 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/ReLU6[5]/11699(MobileNetV2::nndct_relu6_83)
        self.module_84 = py_nndct.nn.Conv2d(in_channels=960, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Sequential[conv]/Conv2d[6]/ret.197(MobileNetV2::nndct_conv2d_84)
        self.module_85 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[15]/Add[skip_add]/ret.201(MobileNetV2::nndct_elemwise_add_85)
        self.module_86 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/Conv2d[0]/ret.203(MobileNetV2::nndct_conv2d_86)
        self.module_87 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/ReLU6[2]/11759(MobileNetV2::nndct_relu6_87)
        self.module_88 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/Conv2d[3]/ret.207(MobileNetV2::nndct_depthwise_conv2d_88)
        self.module_89 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/ReLU6[5]/11789(MobileNetV2::nndct_relu6_89)
        self.module_90 = py_nndct.nn.Conv2d(in_channels=960, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Sequential[conv]/Conv2d[6]/ret.211(MobileNetV2::nndct_conv2d_90)
        self.module_91 = py_nndct.nn.Add() #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[16]/Add[skip_add]/ret.215(MobileNetV2::nndct_elemwise_add_91)
        self.module_92 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/Conv2d[0]/ret.217(MobileNetV2::nndct_conv2d_92)
        self.module_93 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/ReLU6[2]/11849(MobileNetV2::nndct_relu6_93)
        self.module_94 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/Conv2d[3]/ret.221(MobileNetV2::nndct_depthwise_conv2d_94)
        self.module_95 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/ReLU6[5]/11879(MobileNetV2::nndct_relu6_95)
        self.module_96 = py_nndct.nn.Conv2d(in_channels=960, out_channels=320, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/InvertedResidual[17]/Sequential[conv]/Conv2d[6]/ret.225(MobileNetV2::nndct_conv2d_96)
        self.module_97 = py_nndct.nn.Conv2d(in_channels=320, out_channels=1280, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #MobileNetV2::MobileNetV2/Sequential[features]/Sequential[18]/Conv2d[0]/ret.229(MobileNetV2::nndct_conv2d_97)
        self.module_98 = py_nndct.nn.Module('nndct_relu6',inplace=True) #MobileNetV2::MobileNetV2/Sequential[features]/Sequential[18]/ReLU6[2]/11936(MobileNetV2::nndct_relu6_98)
        self.module_99 = py_nndct.nn.AdaptiveAvgPool2d(output_size=[1, 1]) #MobileNetV2::MobileNetV2/AdaptiveAvgPool2d[adp_avgpool]/11953(MobileNetV2::nndct_adaptive_avg_pool2d_99)
        self.module_100 = py_nndct.nn.Module('nndct_shape') #MobileNetV2::MobileNetV2/11956(MobileNetV2::nndct_shape_100)
        self.module_101 = py_nndct.nn.Module('nndct_reshape') #MobileNetV2::MobileNetV2/ret.235(MobileNetV2::nndct_reshape_101)
        self.module_102 = py_nndct.nn.Linear(in_features=1280, out_features=3, bias=True) #MobileNetV2::MobileNetV2/Linear[classifier]/ret.237(MobileNetV2::nndct_dense_102)
        self.module_103 = py_nndct.nn.dequant_output() #MobileNetV2::MobileNetV2/DeQuantStub[dequant_stub]/11969(MobileNetV2::nndct_dequant_stub_103)

    @py_nndct.nn.forward_processor
    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(input=output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_3(output_module_0)
        output_module_0 = self.module_4(output_module_0)
        output_module_0 = self.module_5(output_module_0)
        output_module_0 = self.module_6(output_module_0)
        output_module_0 = self.module_7(output_module_0)
        output_module_0 = self.module_8(output_module_0)
        output_module_0 = self.module_9(output_module_0)
        output_module_0 = self.module_10(output_module_0)
        output_module_0 = self.module_11(output_module_0)
        output_module_12 = self.module_12(output_module_0)
        output_module_12 = self.module_13(output_module_12)
        output_module_12 = self.module_14(output_module_12)
        output_module_12 = self.module_15(output_module_12)
        output_module_12 = self.module_16(output_module_12)
        output_module_17 = self.module_17(input=output_module_0, other=output_module_12, alpha=1)
        output_module_17 = self.module_18(output_module_17)
        output_module_17 = self.module_19(output_module_17)
        output_module_17 = self.module_20(output_module_17)
        output_module_17 = self.module_21(output_module_17)
        output_module_17 = self.module_22(output_module_17)
        output_module_23 = self.module_23(output_module_17)
        output_module_23 = self.module_24(output_module_23)
        output_module_23 = self.module_25(output_module_23)
        output_module_23 = self.module_26(output_module_23)
        output_module_23 = self.module_27(output_module_23)
        output_module_28 = self.module_28(input=output_module_17, other=output_module_23, alpha=1)
        output_module_29 = self.module_29(output_module_28)
        output_module_29 = self.module_30(output_module_29)
        output_module_29 = self.module_31(output_module_29)
        output_module_29 = self.module_32(output_module_29)
        output_module_29 = self.module_33(output_module_29)
        output_module_34 = self.module_34(input=output_module_28, other=output_module_29, alpha=1)
        output_module_34 = self.module_35(output_module_34)
        output_module_34 = self.module_36(output_module_34)
        output_module_34 = self.module_37(output_module_34)
        output_module_34 = self.module_38(output_module_34)
        output_module_34 = self.module_39(output_module_34)
        output_module_40 = self.module_40(output_module_34)
        output_module_40 = self.module_41(output_module_40)
        output_module_40 = self.module_42(output_module_40)
        output_module_40 = self.module_43(output_module_40)
        output_module_40 = self.module_44(output_module_40)
        output_module_45 = self.module_45(input=output_module_34, other=output_module_40, alpha=1)
        output_module_46 = self.module_46(output_module_45)
        output_module_46 = self.module_47(output_module_46)
        output_module_46 = self.module_48(output_module_46)
        output_module_46 = self.module_49(output_module_46)
        output_module_46 = self.module_50(output_module_46)
        output_module_51 = self.module_51(input=output_module_45, other=output_module_46, alpha=1)
        output_module_52 = self.module_52(output_module_51)
        output_module_52 = self.module_53(output_module_52)
        output_module_52 = self.module_54(output_module_52)
        output_module_52 = self.module_55(output_module_52)
        output_module_52 = self.module_56(output_module_52)
        output_module_57 = self.module_57(input=output_module_51, other=output_module_52, alpha=1)
        output_module_57 = self.module_58(output_module_57)
        output_module_57 = self.module_59(output_module_57)
        output_module_57 = self.module_60(output_module_57)
        output_module_57 = self.module_61(output_module_57)
        output_module_57 = self.module_62(output_module_57)
        output_module_63 = self.module_63(output_module_57)
        output_module_63 = self.module_64(output_module_63)
        output_module_63 = self.module_65(output_module_63)
        output_module_63 = self.module_66(output_module_63)
        output_module_63 = self.module_67(output_module_63)
        output_module_68 = self.module_68(input=output_module_57, other=output_module_63, alpha=1)
        output_module_69 = self.module_69(output_module_68)
        output_module_69 = self.module_70(output_module_69)
        output_module_69 = self.module_71(output_module_69)
        output_module_69 = self.module_72(output_module_69)
        output_module_69 = self.module_73(output_module_69)
        output_module_74 = self.module_74(input=output_module_68, other=output_module_69, alpha=1)
        output_module_74 = self.module_75(output_module_74)
        output_module_74 = self.module_76(output_module_74)
        output_module_74 = self.module_77(output_module_74)
        output_module_74 = self.module_78(output_module_74)
        output_module_74 = self.module_79(output_module_74)
        output_module_80 = self.module_80(output_module_74)
        output_module_80 = self.module_81(output_module_80)
        output_module_80 = self.module_82(output_module_80)
        output_module_80 = self.module_83(output_module_80)
        output_module_80 = self.module_84(output_module_80)
        output_module_85 = self.module_85(input=output_module_74, other=output_module_80, alpha=1)
        output_module_86 = self.module_86(output_module_85)
        output_module_86 = self.module_87(output_module_86)
        output_module_86 = self.module_88(output_module_86)
        output_module_86 = self.module_89(output_module_86)
        output_module_86 = self.module_90(output_module_86)
        output_module_91 = self.module_91(input=output_module_85, other=output_module_86, alpha=1)
        output_module_91 = self.module_92(output_module_91)
        output_module_91 = self.module_93(output_module_91)
        output_module_91 = self.module_94(output_module_91)
        output_module_91 = self.module_95(output_module_91)
        output_module_91 = self.module_96(output_module_91)
        output_module_91 = self.module_97(output_module_91)
        output_module_91 = self.module_98(output_module_91)
        output_module_91 = self.module_99(output_module_91)
        output_module_100 = self.module_100(input=output_module_91, dim=0)
        output_module_101 = self.module_101(input=output_module_91, shape=[output_module_100,-1])
        output_module_101 = self.module_102(output_module_101)
        output_module_101 = self.module_103(input=output_module_101)
        return output_module_101
