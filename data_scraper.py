raw_data = """
Product,Status,Release Date,Cores,Threads,Lithography(nm),Max. Turbo Freq.(GHz),Base Freq.(GHz),Cache(MB),TDP(W),Cache Info,Integrated Graphics
Core i7-7740X X Series,Discontinued,Q2'17,4,8,14,4.50,4.30,112,8,N/A,N/A
Core i5-7640X X Series,Discontinued,Q2'17,4,4,14,4.20,4.00,112,6,N/A,N/A
Core i7-7800X X Series,Discontinued,Q2'17,6,12,14,4.00,3.50,140,8.25,L3 Cache,N/A
Core i9-7900X X Series,Discontinued,Q2'17,10,20,14,4.30,3.30,140,13.75,L3 Cache,N/A
Core i7-7820X X Series,Discontinued,Q2'17,8,16,14,4.30,3.60,140,11,L3 Cache,N/A
Core i9-7920X X Series,Discontinued,Q3'17,12,24,14,4.30,2.90,140,16.5,L3 Cache,N/A
Core i9-7940X X Series,Discontinued,Q3'17,14,28,N/A,4.30,3.10,165,19.25,N/A,N/A
Core i9-7960X X Series,Discontinued,Q3'17,16,32,N/A,4.20,2.80,165,22,N/A,N/A
Core i9-7980XE Extreme Edition,Discontinued,Q3'17,18,36,N/A,4.20,2.60,165,24.75,N/A,N/A
Core i9-9820X X Series,Discontinued,Q4'18,10,20,14,4.10,3.30,165,16.5,Intel Smart Cache,N/A
Core i7-9800X X Series,Discontinued,Q4'18,8,16,14,4.40,3.80,165,16.5,Intel Smart Cache,N/A
Core i9-9960X X Series,Discontinued,Q4'18,16,32,14,4.40,3.10,165,22,Intel Smart Cache,N/A
Core i9-9900X X Series,Discontinued,Q4'18,10,20,14,4.40,3.50,165,19.25,Intel Smart Cache,N/A
Core i9-9940X X Series,Discontinued,Q4'18,14,28,14,4.40,3.30,165,19.25,Intel Smart Cache,N/A
Core i9-9980XE Extreme Edition,Discontinued,Q4'18,18,36,14,4.40,3.00,165,24.75,Intel Smart Cache,N/A
Core i9-9920X X Series,Discontinued,Q4'18,12,24,14,4.40,3.50,165,19.25,Intel Smart Cache,N/A
Core i9-10920X X Series,Launched,Q4'19,12,24,14,4.60,3.50,165,19.25,Intel Smart Cache,N/A
Core i9-10940X X Series,Launched,Q4'19,14,28,14,4.60,3.30,165,19.25,Intel Smart Cache,N/A
Core i9-10980XE Extreme Edition,Launched,Q4'19,18,36,14,4.60,3.00,165,24.75,Intel Smart Cache,N/A
Core i9-10900X X Series,Launched,Q4'19,10,20,14,4.50,3.70,165,19.25,Intel Smart Cache,N/A
Core i7-3960X Extreme Edition,Discontinued,Q4'11,6,12,32,3.90,3.30,130,15,Intel Smart Cache,N/A
Core i7-3930K,Discontinued,Q4'11,6,12,32,3.80,3.20,130,12,Intel Smart Cache,N/A
Core i7-3820,Discontinued,Q1'12,4,8,32,3.80,3.60,130,10,Intel Smart Cache,N/A
Core i7-3920XM Extreme Edition,Discontinued,Q2'12,4,8,22,3.80,2.90,55,8,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3970X Extreme Edition,Discontinued,Q4'12,6,12,32,4.00,3.50,150,15,Intel Smart Cache,N/A
Core i7-3940XM Extreme Edition,Discontinued,Q3'12,4,8,22,3.90,3.00,55,8,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-4930MX Extreme Edition,Discontinued,Q2'13,4,8,22,3.90,3.00,57,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4960X Extreme Edition,Discontinued,Q3'13,6,12,22,4.00,3.60,130,15,Intel Smart Cache,N/A
Core i7-4930K,Discontinued,Q3'13,6,12,22,3.90,3.40,130,12,Intel Smart Cache,N/A
Core i7-4820K,Discontinued,Q3'13,4,8,22,3.90,3.70,130,10,Intel Smart Cache,N/A
Core i7-4940MX Extreme Edition,Discontinued,Q1'14,4,8,22,4.00,3.10,57,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-5960X Extreme Edition,Discontinued,Q3'14,8,16,22,3.50,3.00,140,20,Intel Smart Cache,N/A
Core i7-5930K,Discontinued,Q3'14,6,12,22,3.70,3.50,140,15,Intel Smart Cache,N/A
Core i7-5820K,Discontinued,Q3'14,6,12,22,3.60,3.30,140,15,Intel Smart Cache,N/A
Core i7-6850K,Discontinued,Q2'16,6,12,14,3.80,3.60,140,15,N/A,N/A
Core i7-6800K,Discontinued,Q2'16,6,12,14,3.60,3.40,140,15,Intel Smart Cache,N/A
Core i7-6900K,Discontinued,Q2'16,8,16,14,3.70,3.20,140,20,N/A,N/A
Core i7-6950X Extreme Edition,Discontinued,Q2'16,10,20,14,3.50,3.00,140,25,N/A,N/A
Core i5-L16G7,Launched,Q2'20,5,5,10,3.00,1.40,7,4,N/A,Intel UHD Graphics
Core i3-L13G4,Launched,Q2'20,5,5,10,2.80,0.80,7,4,N/A,Intel UHD Graphics
Core i9-12900K,Launched,Q4'21,16,24,7,5.20,3.20,125,30,Intel Smart Cache,Intel UHD Graphics 770
Core i9-12900KF,Launched,Q4'21,16,24,7,5.20,3.20,125,30,Intel Smart Cache,N/A
Core i9-11900,Launched,Q1'21,8,16,14,5.20,2.50,65,16,Intel Smart Cache,Intel UHD Graphics 750
Core i9-11900F,Launched,Q1'21,8,16,14,5.20,2.50,65,16,Intel Smart Cache,N/A
Core i9-11900T,Launched,Q1'21,8,16,14,4.90,1.50,35,16,Intel Smart Cache,Intel UHD Graphics 750
Core i9-11900KF,Launched,Q1'21,8,16,14,5.30,3.50,125,16,Intel Smart Cache,N/A
Core i9-11900K,Launched,Q1'21,8,16,14,5.30,3.50,125,16,Intel Smart Cache,Intel UHD Graphics 750
Core i9-11950H,Launched,Q2'21,8,16,10,5.00,N/A,N/A,24,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i9-11980HK,Launched,Q2'21,8,16,10,5.00,N/A,N/A,24,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i9-11900H,Launched,Q2'21,8,16,10,4.90,N/A,N/A,24,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i9-10900T,Launched,Q2'20,10,20,14,4.60,1.90,35,20,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-10900,Launched,Q2'20,10,20,14,5.20,2.80,65,20,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-10900F,Launched,Q2'20,10,20,14,5.20,2.80,65,20,Intel Smart Cache,N/A
Core i9-10900KF,Launched,Q2'20,10,20,14,5.30,3.70,125,20,Intel Smart Cache,N/A
Core i9-10900K,Launched,Q2'20,10,20,14,5.30,3.70,125,20,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-10980HK,Launched,Q2'20,8,16,14,5.30,2.40,45,16,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i9-10885H,Launched,Q2'20,8,16,14,5.30,2.40,45,16,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i9-10900TE,Launched,Q2'20,10,20,14,4.50,1.80,35,20,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-10900E,Launched,Q2'20,10,20,14,4.70,2.80,65,20,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-10850K,Launched,Q3'20,10,20,14,5.20,3.60,125,20,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-9900K,Launched,Q4'18,8,16,14,5.00,3.60,95,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-9900KF,Launched,Q1'19,8,16,14,5.00,3.60,95,16,Intel Smart Cache,N/A
Core i9-9900T,Launched,Q2'19,8,16,14,4.40,2.10,35,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-9900,Launched,Q2'19,8,16,14,5.00,3.10,65,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-9900KS,Discontinued,Q4'19,8,16,14,5.00,4.00,127,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-9880H,Launched,Q2'19,8,16,14,4.80,2.30,45,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-9980HK,Launched,Q2'19,8,16,14,5.00,2.40,45,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i9-8950HK,Launched,Q2'18,6,12,14,4.80,2.90,45,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-12700K,Launched,Q4'21,12,20,7,5.00,3.60,125,25,Intel Smart Cache,Intel UHD Graphics 770
Core i7-12700KF,Launched,Q4'21,12,20,7,5.00,3.60,125,25,Intel Smart Cache,N/A
Core i7-11370H,Launched,Q1'21,4,8,10,4.80,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-11375H,Launched,Q1'21,4,8,10,5.00,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-1185G7E,Launched,Q3'20,4,8,10,4.40,1.80,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-1185GRE,Launched,Q3'20,4,8,10,4.40,1.80,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-1160G7,Launched,Q3'20,4,8,10,4.40,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-1165G7,Launched,Q3'20,4,8,10,4.70,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-1180G7,Launched,Q1'21,4,8,10,4.60,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-1185G7,Launched,Q3'20,4,8,10,4.80,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-1165G7 (with IPU),Launched,Q3'20,4,8,10,4.70,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics
Core i7-11700K,Launched,Q1'21,8,16,14,5.00,3.60,125,16,Intel Smart Cache,Intel UHD Graphics 750
Core i7-11700KF,Launched,Q1'21,8,16,14,5.00,3.60,125,16,Intel Smart Cache,N/A
Core i7-11700T,Launched,Q1'21,8,16,14,4.60,1.40,35,16,Intel Smart Cache,Intel UHD Graphics 750
Core i7-11700,Launched,Q1'21,8,16,14,4.90,2.50,65,16,Intel Smart Cache,Intel UHD Graphics 750
Core i7-11700F,Launched,Q1'21,8,16,14,4.90,2.50,65,16,Intel Smart Cache,N/A
Core i7-11850H,Launched,Q2'21,8,16,10,4.80,N/A,N/A,24,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i7-11600H,Launched,Q3'21,6,12,10,4.60,N/A,N/A,18,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i7-11800H,Launched,Q2'21,8,16,10,4.60,N/A,N/A,24,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i7-1195G7 (with IPU),Launched,Q2'21,4,8,10,5.00,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics eligible
Core i7-11390H,Launched,Q2'21,4,8,10,5.00,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics eligible
Core i7-1195G7,Launched,Q2'21,4,8,10,5.00,N/A,N/A,12,Intel Smart Cache,Intel Iris Xe Graphics eligible
Core i7-11850HE,Launched,Q3'21,8,16,10,4.70,N/A,N/A,24,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i7-10710U,Launched,Q3'19,6,12,14,4.70,1.10,15,12,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-10510U,Launched,Q3'19,4,8,14,4.90,1.80,15,8,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-10510Y,Launched,Q3'19,4,8,14,4.50,1.20,7,8,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-1068NG7,Launched,Q2'20,4,8,10,4.10,2.30,28,8,Intel Smart Cache,Intel Iris Plus Graphics
Core i7-1065G7,Launched,Q3'19,4,8,10,3.90,1.30,15,8,Intel Smart Cache,Intel Iris Plus Graphics
Core i7-1060G7,Launched,Q3'19,4,8,10,3.80,1.00,9,8,Intel Smart Cache,Intel Iris Plus Graphics
Core i7-10700T,Launched,Q2'20,8,16,14,4.50,2.00,35,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-10700,Launched,Q2'20,8,16,14,4.80,2.90,65,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-10700F,Launched,Q2'20,8,16,14,4.80,2.90,65,16,Intel Smart Cache,N/A
Core i7-10700KF,Launched,Q2'20,8,16,14,5.10,3.80,125,16,Intel Smart Cache,N/A
Core i7-10700K,Launched,Q2'20,8,16,14,5.10,3.80,125,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-10750H,Launched,Q2'20,6,12,14,5.00,2.60,45,12,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-10810U,Launched,Q2'20,6,12,14,4.90,1.10,15,12,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-10610U,Launched,Q2'20,4,8,14,4.90,1.80,15,8,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-10850H,Launched,Q2'20,6,12,14,5.10,2.70,45,12,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-10875H,Launched,Q2'20,8,16,14,5.10,2.30,45,16,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-10700TE,Launched,Q2'20,8,16,14,4.40,2.00,35,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-10700E,Launched,Q2'20,8,16,14,4.50,2.90,65,16,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-10870H,Launched,Q3'20,8,16,14,5.00,2.20,45,16,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i7-9700K,Launched,Q4'18,8,8,14,4.90,3.60,95,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-9700KF,Launched,Q1'19,8,8,14,4.90,3.60,95,12,Intel Smart Cache,N/A
Core i7-9750H,Launched,Q2'19,6,12,14,4.50,2.60,45,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-9750HF,Launched,Q2'19,6,12,14,4.50,2.60,45,12,Intel Smart Cache,N/A
Core i7-9850H,Launched,Q2'19,6,12,14,4.60,2.60,45,12,N/A,Intel UHD 630 Graphics
Core i7-9700T,Launched,Q2'19,8,8,14,4.30,2.00,35,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-9700,Launched,Q2'19,8,8,14,4.70,3.00,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-9700F,Launched,Q2'19,8,8,14,4.70,3.00,65,12,Intel Smart Cache,N/A
Core i7-9700E,Launched,Q2'19,8,8,14,4.40,2.60,65,12,N/A,Intel UHD 630 Graphics
Core i7-9850HE,Launched,Q2'19,6,12,14,4.40,2.70,45,9,N/A,Intel UHD 630 Graphics
Core i7-9700TE,Launched,Q2'19,8,8,14,3.80,1.80,35,12,N/A,Intel UHD 630 Graphics
Core i7-9850HL,Launched,Q2'19,6,12,14,4.10,1.90,25,9,N/A,Intel UHD 630 Graphics
Core i7-8550U,Launched,Q3'17,4,8,14,4.00,1.80,15,8,Intel Smart Cache,Intel UHD 620 Graphics
Core i7-8650U,Launched,Q3'17,4,8,14,4.20,1.90,15,8,Intel Smart Cache,Intel UHD 620 Graphics
Core i7-8700K,Discontinued,Q4'17,6,12,14,4.70,3.70,95,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-8700,Launched,Q4'17,6,12,14,4.60,3.20,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-8700T,Launched,Q2'18,6,12,14,4.00,2.40,35,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-8706G with Radeon RX Vega M GL Graphics,Launched,Q1'18,4,8,14,4.10,3.10,N/A,8,N/A,Intel HD 630 Graphics
Core i7-8709G with Radeon RX Vega M GH Graphics,Discontinued,Q1'18,4,8,14,4.10,3.10,N/A,8,N/A,Intel HD 630 Graphics
Core i7-8809G with Radeon RX Vega M GH Graphics,Discontinued,Q1'18,4,8,14,4.20,3.10,N/A,8,N/A,Intel HD 630 Graphics
Core i7-8705G with Radeon RX Vega M GL Graphics,Discontinued,Q1'18,4,8,14,4.10,3.10,N/A,8,N/A,Intel HD 630 Graphics
Core i7-8850H,Launched,Q2'18,6,12,14,4.30,2.60,45,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-8700B,Launched,Q2'18,6,12,14,4.60,3.20,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-8750H,Launched,Q2'18,6,12,14,4.10,2.20,45,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-8559U,Launched,Q2'18,4,8,14,4.50,2.70,28,8,Intel Smart Cache,Intel Iris Plus Graphics 655
Core i7+8700 Includes Intel Optane Memory,Launched,Q2'18,6,12,14,4.60,3.20,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-8086K,Launched,Q2'18,6,12,14,5.00,4.00,95,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i7-8706G with Radeon Pro WX Vega M GL Graphics,Discontinued,Q3'18,4,8,14,4.10,3.10,N/A,8,N/A,Intel HD 630 Graphics
Core i7-8565U,Launched,Q3'18,4,8,14,4.60,1.80,15,8,Intel Smart Cache,Intel UHD Graphics for 8th Generation Intel Core Processors
Core i7-8500Y,Launched,Q1'19,2,4,14,4.20,1.50,5,4,Intel Smart Cache,Intel UHD 615 Graphics
Core i7-8569U,Launched,Q2'19,4,8,14,4.70,2.80,28,8,Intel Smart Cache,Intel Iris Plus Graphics 655
Core i7-8557U,Launched,Q3'19,4,8,14,4.50,1.70,15,8,Intel Smart Cache,Intel Iris Plus Graphics 645
Core i7-8665UE,Launched,Q2'19,4,8,14,4.40,1.70,15,8,Intel Smart Cache,Intel UHD 620 Graphics
Core i7-8665U,Launched,Q2'19,4,8,14,4.80,1.90,15,8,Intel Smart Cache,Intel UHD Graphics for 8th Generation Intel Core Processors
Core i7-7Y75,Launched,Q3'16,2,4,14,3.60,1.30,4.5,4,Intel Smart Cache,Intel HD 615 Graphics
Core i7-7500U,Launched,Q3'16,2,4,14,3.50,2.70,15,4,Intel Smart Cache,Intel HD 620 Graphics
Core i7-7700T,Launched,Q1'17,4,8,14,3.80,2.90,35,8,Intel Smart Cache,Intel HD 630 Graphics
Core i7-7820EQ,Launched,Q1'17,4,8,14,3.70,3.00,45,8,N/A,Intel HD 630 Graphics
Core i7-7700,Launched,Q1'17,4,8,14,4.20,3.60,65,8,Intel Smart Cache,Intel HD 630 Graphics
Core i7-7700K,Discontinued,Q1'17,4,8,14,4.50,4.20,91,8,Intel Smart Cache,Intel HD 630 Graphics
Core i7-7700HQ,Launched,Q1'17,4,8,14,3.80,2.80,45,6,N/A,Intel HD 630 Graphics
Core i7-7920HQ,Launched,Q1'17,4,8,14,4.10,3.10,45,8,N/A,Intel HD 630 Graphics
Core i7-7820HK,Launched,Q1'17,4,8,14,3.90,2.90,45,8,N/A,Intel HD 630 Graphics
Core i7-7600U,Launched,Q1'17,2,4,14,3.90,2.80,15,4,Intel Smart Cache,Intel HD 620 Graphics
Core i7-7820HQ,Launched,Q1'17,4,8,14,3.90,2.90,45,8,N/A,Intel HD 630 Graphics
Core i7-7660U,Launched,Q1'17,2,4,14,4.00,2.50,15,4,N/A,Intel Iris Plus 640 Graphics
Core i7-7560U,Launched,Q1'17,2,4,14,3.80,2.40,15,4,N/A,Intel Iris Plus 640 Graphics
Core i7-7567U,Launched,Q1'17,2,4,14,4.00,3.50,28,4,N/A,Intel Iris Plus 650 Graphics
Core i7-6600U,Launched,Q3'15,2,4,14,3.40,2.60,15,4,Intel Smart Cache,Intel HD 520 Graphics
Core i7-6500U,Discontinued,Q3'15,2,4,14,3.10,2.50,15,4,Intel Smart Cache,Intel HD 520 Graphics
Core i7-6700K,Discontinued,Q3'15,4,8,14,4.20,4.00,91,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6700,Launched,Q3'15,4,8,14,4.00,3.40,65,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6700T,Launched,Q3'15,4,8,14,3.60,2.80,35,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6700TE,Launched,Q4'15,4,8,14,3.40,2.40,35,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6700HQ,Discontinued,Q3'15,4,8,14,3.50,2.60,45,6,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6820HK,Discontinued,Q3'15,4,8,14,3.60,2.70,45,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6820HQ,Discontinued,Q3'15,4,8,14,3.60,2.70,45,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6920HQ,Discontinued,Q3'15,4,8,14,3.80,2.90,45,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6820EQ,Launched,Q4'15,4,8,14,3.50,2.80,45,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6822EQ,Launched,Q4'15,4,8,14,2.80,2.00,25,8,Intel Smart Cache,Intel HD 530 Graphics
Core i7-6560U,Discontinued,Q3'15,2,4,14,3.20,2.20,15,4,Intel Smart Cache,Intel Iris 540 Graphics
Core i7-6567U,Discontinued,Q3'15,2,4,14,3.60,3.30,28,4,Intel Smart Cache,Intel Iris 550 Graphics
Core i7-6660U,Discontinued,Q1'16,2,4,14,3.40,2.40,15,4,Intel Smart Cache,Intel Iris 540 Graphics
Core i7-6650U,Discontinued,Q3'15,2,4,14,3.40,2.20,15,4,Intel Smart Cache,Intel Iris 540 Graphics
Core i7-6970HQ,Discontinued,Q1'16,4,8,14,3.70,2.80,45,8,Intel Smart Cache,Intel Iris Pro 580 Graphics
Core i7-6785R,Discontinued,Q2'16,4,8,14,3.90,3.30,65,8,N/A,Intel Iris Pro 580 Graphics
Core i7-6870HQ,Discontinued,Q1'16,4,8,14,3.60,2.70,45,8,Intel Smart Cache,Intel Iris Pro 580 Graphics
Core i7-6770HQ,Discontinued,Q1'16,4,8,14,3.50,2.60,45,6,Intel Smart Cache,Intel Iris Pro 580 Graphics
Core i7-5550U,Discontinued,Q1'15,2,4,14,3.00,2.00,15,4,Intel Smart Cache,Intel HD 6000 Graphics
Core i7-5557U,Discontinued,Q1'15,2,4,14,3.40,3.10,28,4,N/A,Intel Iris 6100 Graphics
Core i7-5650U,Launched,Q1'15,2,4,14,3.10,2.20,15,4,N/A,Intel HD 6000 Graphics
Core i7-5500U,Discontinued,Q1'15,2,4,14,3.00,2.40,15,4,N/A,Intel HD 5500 Graphics
Core i7-5600U,Discontinued,Q1'15,2,4,14,3.20,2.60,15,4,N/A,Intel HD 5500 Graphics
Core i7-5700HQ,Discontinued,Q2'15,4,8,14,3.50,2.70,47,6,N/A,Intel Iris Pro 6200 Graphics
Core i7-5750HQ,Discontinued,Q2'15,4,8,14,3.40,2.50,47,6,N/A,Intel Iris Pro 6200 Graphics
Core i7-5775R,Discontinued,Q2'15,4,8,14,3.80,3.30,65,6,N/A,Intel Iris Pro 6200 Graphics
Core i7-5850HQ,Discontinued,Q2'15,4,8,14,3.60,2.70,47,6,N/A,Intel Iris Pro 6200 Graphics
Core i7-5950HQ,Discontinued,Q2'15,4,8,14,3.80,2.90,47,6,N/A,Intel Iris Pro 6200 Graphics
Core i7-5775C,Discontinued,Q2'15,4,8,14,3.70,3.30,65,6,N/A,Intel Iris Pro 6200 Graphics
Core i7-5700EQ,Launched,Q2'15,4,8,14,3.40,2.60,47,6,Intel Smart Cache,Intel Iris Pro 6200 Graphics
Core i7-5850EQ,Launched,Q2'15,4,8,14,3.40,2.70,47,6,Intel Smart Cache,Intel Iris Pro 6200 Graphics
Core i7-4550U,Discontinued,Q3'13,2,4,22,3.00,1.50,15,4,Intel Smart Cache,Intel HD 5000 Graphics
Core i7-4650U,Launched,Q3'13,2,4,22,3.30,1.70,15,4,Intel Smart Cache,Intel HD 5000 Graphics
Core i7-4700HQ,Discontinued,Q2'13,4,8,22,3.40,2.40,47,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4700MQ,Discontinued,Q2'13,4,8,22,3.40,2.40,47,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4702HQ,Discontinued,Q2'13,4,8,22,3.20,2.20,37,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4702MQ,Discontinued,Q2'13,4,8,22,3.20,2.20,37,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4765T,Discontinued,Q2'13,4,8,22,3.00,2.00,35,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4770,Discontinued,Q2'13,4,8,22,3.90,3.40,84,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4770K,Discontinued,Q2'13,4,8,22,3.90,3.50,84,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4770S,Launched,Q2'13,4,8,22,3.90,3.10,65,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4770T,Discontinued,Q2'13,4,8,22,3.70,2.50,45,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4800MQ,Discontinued,Q2'13,4,8,22,3.70,2.70,47,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4900MQ,Discontinued,Q2'13,4,8,22,3.80,2.80,47,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4500U,Discontinued,Q3'13,2,4,22,3.00,1.80,15,4,Intel Smart Cache,Intel HD 4400 Graphics
Core i7-4700EQ,Launched,Q2'13,4,8,22,3.40,2.40,47,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4700EC,Launched,Q1'14,4,8,22,N/A,2.70,43,8,Intel Smart Cache,N/A
Core i7-4702EC,Launched,Q1'14,4,8,22,N/A,2.00,27,8,Intel Smart Cache,N/A
Core i7-4770TE,Launched,Q2'13,4,8,22,3.30,2.30,45,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4558U,Discontinued,Q3'13,2,4,22,3.30,2.80,28,4,Intel Smart Cache,Intel Iris 5100 Graphics
Core i7-4950HQ,Discontinued,Q3'13,4,8,22,3.60,2.40,47,6,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i7-4850HQ,Discontinued,Q3'13,4,8,22,3.50,2.30,47,6,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i7-4750HQ,Discontinued,Q3'13,4,8,22,3.20,2.00,47,6,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i7-4960HQ,Discontinued,Q4'13,4,8,22,3.80,2.60,47,6,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i7-4860HQ,Discontinued,Q1'14,4,8,22,3.60,2.40,47,6,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i7-4760HQ,Discontinued,Q2'14,4,8,22,3.30,2.10,47,6,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i7-4600M,Discontinued,Q4'13,2,4,22,3.60,2.90,37,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4600U,Discontinued,Q3'13,2,4,22,3.30,2.10,15,4,Intel Smart Cache,Intel HD 4400 Graphics
Core i7-4610Y,Discontinued,Q3'13,2,4,22,2.90,1.70,11.5,4,Intel Smart Cache,Intel HD 4200 Graphics
Core i7-4770R,Discontinued,Q2'13,4,8,22,3.90,3.20,65,6,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i7-4771,Discontinued,Q3'13,4,8,22,3.90,3.50,84,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4710HQ,Discontinued,Q2'14,4,8,22,3.50,2.50,47,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4710MQ,Discontinued,Q2'14,4,8,22,3.50,2.50,47,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4712HQ,Discontinued,Q2'14,4,8,22,3.30,2.30,37,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4712MQ,Discontinued,Q2'14,4,8,22,3.30,2.30,37,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4720HQ,Discontinued,Q1'15,4,8,22,3.60,2.60,47,6,N/A,Intel HD 4600 Graphics
Core i7-4722HQ,Discontinued,Q1'15,4,8,22,3.40,2.40,37,6,N/A,Intel HD 4600 Graphics
Core i7-4810MQ,Discontinued,Q1'14,4,8,22,3.80,2.80,47,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4910MQ,Discontinued,Q1'14,4,8,22,3.90,2.90,47,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4610M,Discontinued,Q1'14,2,4,22,3.70,3.00,37,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4790,Discontinued,Q2'14,4,8,22,4.00,3.60,84,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4790K,Discontinued,Q2'14,4,8,22,4.40,4.00,88,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4790S,Launched,Q2'14,4,8,22,4.00,3.20,65,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4790T,Discontinued,Q2'14,4,8,22,3.90,2.70,45,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4785T,Discontinued,Q2'14,4,8,22,3.20,2.20,35,8,Intel Smart Cache,Intel HD 4600 Graphics
Core i7-4510U,Discontinued,Q2'14,2,4,22,3.10,2.00,15,4,Intel Smart Cache,Intel HD 4400 Graphics
Core i7-4980HQ,Discontinued,Q3'14,4,8,22,4.00,2.80,47,6,N/A,Intel Iris Pro 5200 Graphics
Core i7-4870HQ,Discontinued,Q3'14,4,8,22,3.70,2.50,47,6,N/A,Intel Iris Pro 5200 Graphics
Core i7-4770HQ,Discontinued,Q3'14,4,8,22,3.40,2.20,47,6,N/A,Intel Iris Pro 5200 Graphics
Core i7-4578U,Discontinued,Q3'14,2,4,22,3.50,3.00,28,4,N/A,Intel Iris 5100 Graphics
Core i5-12600K,Launched,Q4'21,10,16,7,4.90,3.70,125,20,Intel Smart Cache,Intel UHD Graphics 770
Core i5-12600KF,Launched,Q4'21,10,16,7,4.90,3.70,125,20,Intel Smart Cache,N/A
Core i5-11300H,Launched,Q1'21,4,8,10,4.40,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics
Core i5-1145GRE,Launched,Q3'20,4,8,10,4.10,1.50,15,8,Intel Smart Cache,Intel Iris Xe Graphics
Core i5-1145G7E,Launched,Q3'20,4,8,10,4.10,1.50,15,8,Intel Smart Cache,Intel Iris Xe Graphics
Core i5-1130G7,Launched,Q3'20,4,8,10,4.00,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics
Core i5-1135G7,Launched,Q3'20,4,8,10,4.20,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics
Core i5-1140G7,Launched,Q1'21,4,8,10,4.20,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics
Core i5-1145G7,Launched,Q1'21,4,8,10,4.40,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics
Core i5-1135G7 (with IPU),Launched,Q3'20,4,8,10,4.20,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics
Core i5-11400,Launched,Q1'21,6,12,14,4.40,2.60,65,12,Intel Smart Cache,Intel UHD Graphics 730
Core i5-11400F,Launched,Q1'21,6,12,14,4.40,2.60,65,12,Intel Smart Cache,N/A
Core i5-11500T,Launched,Q1'21,6,12,14,3.90,1.50,35,12,Intel Smart Cache,Intel UHD Graphics 750
Core i5-11400T,Launched,Q1'21,6,12,14,3.70,1.30,35,12,Intel Smart Cache,Intel UHD Graphics 730
Core i5-11600,Launched,Q1'21,6,12,14,4.80,2.80,65,12,Intel Smart Cache,Intel UHD Graphics 750
Core i5-11600K,Launched,Q1'21,6,12,14,4.90,3.90,125,12,Intel Smart Cache,Intel UHD Graphics 750
Core i5-11600KF,Launched,Q1'21,6,12,14,4.90,3.90,125,12,Intel Smart Cache,N/A
Core i5-11500,Launched,Q1'21,6,12,14,4.60,2.70,65,12,Intel Smart Cache,Intel UHD Graphics 750
Core i5-11600T,Launched,Q1'21,6,12,14,4.10,1.70,35,12,Intel Smart Cache,Intel UHD Graphics 750
Core i5-11500H,Launched,Q2'21,6,12,10,4.60,N/A,N/A,12,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i5-11400H,Launched,Q2'21,6,12,10,4.50,N/A,N/A,12,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i5-11260H,Launched,Q2'21,6,12,10,4.40,N/A,N/A,12,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i5-11320H,Launched,Q2'21,4,8,10,4.50,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics eligible
Core i5-1155G7 (with IPU),Launched,Q2'21,4,8,10,4.50,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics eligible
Core i5-1155G7,Launched,Q2'21,4,8,10,4.50,N/A,N/A,8,Intel Smart Cache,Intel Iris Xe Graphics eligible
Core i5-11500HE,Launched,Q3'21,6,12,10,4.50,N/A,N/A,12,Intel Smart Cache,Intel UHD Graphics for 11th Generation Intel Core Processors
Core i5-10210U,Launched,Q3'19,4,8,14,4.20,1.60,15,6,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-10310Y,Discontinued,Q3'19,4,8,14,4.10,1.10,7,6,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-10210Y,Launched,Q3'19,4,8,14,4.00,1.00,7,6,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-1035G4,Launched,Q3'19,4,8,10,3.70,1.10,15,6,Intel Smart Cache,Intel Iris Plus Graphics
Core i5-1035G7,Launched,Q3'19,4,8,10,3.70,1.20,15,6,Intel Smart Cache,Intel Iris Plus Graphics
Core i5-1038NG7,Launched,Q2'20,4,8,10,3.80,2.00,28,6,Intel Smart Cache,Intel Iris Plus Graphics
Core i5-1035G1,Launched,Q3'19,4,8,10,3.60,1.00,15,6,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-1030G7,Discontinued,Q3'19,4,8,10,3.50,0.80,9,6,Intel Smart Cache,Intel Iris Plus Graphics
Core i5-1030G4,Discontinued,Q3'19,4,8,10,3.50,0.70,9,6,Intel Smart Cache,Intel Iris Plus Graphics
Core i5-10400,Launched,Q2'20,6,12,14,4.30,2.90,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10600,Launched,Q2'20,6,12,14,4.80,3.30,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10500T,Launched,Q2'20,6,12,14,3.80,2.30,35,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10400T,Launched,Q2'20,6,12,14,3.60,2.00,35,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10500,Launched,Q2'20,6,12,14,4.50,3.10,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10400F,Launched,Q2'20,6,12,14,4.30,2.90,65,12,Intel Smart Cache,N/A
Core i5-10600T,Launched,Q2'20,6,12,14,4.00,2.40,35,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10600K,Launched,Q2'20,6,12,14,4.80,4.10,125,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10600KF,Launched,Q2'20,6,12,14,4.80,4.10,125,12,Intel Smart Cache,N/A
Core i5-10300H,Launched,Q2'20,4,8,14,4.50,2.50,45,8,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-10505,Launched,Q1'21,6,12,14,4.60,3.20,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10310U,Launched,Q2'20,4,8,14,4.40,1.70,15,6,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-10400H,Launched,Q2'20,4,8,14,4.60,2.60,45,8,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-10500H,Launched,Q4'20,6,12,14,4.50,2.50,45,12,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-10500TE,Launched,Q2'20,6,12,14,3.70,2.30,35,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10500E,Launched,Q2'20,6,12,14,4.20,3.10,65,12,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-10200H,Launched,Q3'20,4,8,14,4.10,2.40,45,8,Intel Smart Cache,Intel UHD Graphics for 10th Generation Intel Core Processors
Core i5-9400T,Launched,Q2'19,6,6,14,3.40,1.80,35,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9500,Launched,Q2'19,6,6,14,4.40,3.00,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9600K,Launched,Q4'18,6,6,14,4.60,3.70,95,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9400,Launched,Q1'19,6,6,14,4.10,2.90,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9600,Launched,Q2'19,6,6,14,4.60,3.10,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9400F,Launched,Q1'19,6,6,14,4.10,2.90,65,9,Intel Smart Cache,N/A
Core i5-9600KF,Launched,Q1'19,6,6,14,4.60,3.70,95,9,Intel Smart Cache,N/A
Core i5-9500F,Launched,Q2'19,6,6,14,4.40,3.00,65,9,Intel Smart Cache,N/A
Core i5-9600T,Launched,Q2'19,6,6,14,3.90,2.30,35,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9500T,Launched,Q2'19,6,6,14,3.70,2.20,35,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9300H,Launched,Q2'19,4,8,14,4.10,2.40,45,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9400H,Launched,Q2'19,4,8,14,4.30,2.50,45,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-9300HF,Launched,Q2'19,4,8,14,4.10,2.40,45,8,Intel Smart Cache,N/A
Core i5-9500E,Launched,Q2'19,6,6,14,4.20,3.00,65,9,N/A,Intel UHD 630 Graphics
Core i5-9500TE,Launched,Q2'19,6,6,14,3.60,2.20,35,9,N/A,Intel UHD 630 Graphics
Core i5-8250U,Launched,Q3'17,4,8,14,3.40,1.60,15,6,Intel Smart Cache,Intel UHD 620 Graphics
Core i5-8350U,Launched,Q3'17,4,8,14,3.60,1.70,15,6,Intel Smart Cache,Intel UHD 620 Graphics
Core i5-8600K,Discontinued,Q4'17,6,6,14,4.30,3.60,95,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8400,Discontinued,Q4'17,6,6,14,4.00,2.80,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8600,Discontinued,Q2'18,6,6,14,4.30,3.10,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8600T,Discontinued,Q2'18,6,6,14,3.70,2.30,35,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8500,Launched,Q2'18,6,6,14,4.10,3.00,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8400T,Discontinued,Q2'18,6,6,14,3.30,1.70,35,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8500T,Launched,Q2'18,6,6,14,3.50,2.10,35,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8305G with Radeon RX Vega M GL Graphics,Announced,Q1'18,4,8,14,3.80,2.80,N/A,6,N/A,Intel HD 630 Graphics
Core i5-8300H,Launched,Q2'18,4,8,14,4.00,2.30,45,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8400H,Launched,Q2'18,4,8,14,4.20,2.50,45,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8400B,Discontinued,Q2'18,6,6,14,4.00,2.80,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8500B,Discontinued,Q2'18,6,6,14,4.10,3.00,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8259U,Launched,Q2'18,4,8,14,3.80,2.30,28,6,Intel Smart Cache,Intel Iris Plus Graphics 655
Core i5-8269U,Launched,Q2'18,4,8,14,4.20,2.60,28,6,Intel Smart Cache,Intel Iris Plus Graphics 655
Core i5+8500 Includes Intel Optane Memory,Launched,Q2'18,6,6,14,4.10,3.00,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5+8400 Includes Intel Optane Memory,Launched,Q2'18,6,6,14,4.00,2.80,65,9,Intel Smart Cache,Intel UHD 630 Graphics
Core i5-8305G with Radeon Pro WX Vega M GL Graphics,Discontinued,Q3'18,4,8,14,3.80,2.80,N/A,6,N/A,Intel HD 630 Graphics
Core i5-8265U,Launched,Q3'18,4,8,14,3.90,1.60,15,6,Intel Smart Cache,Intel UHD Graphics for 8th Generation Intel Processors
Core i5-8200Y,Launched,Q3'18,2,4,14,3.90,1.30,5,4,Intel Smart Cache,Intel UHD 615 Graphics
Core i5-8210Y,Discontinued,Q1'19,2,4,14,3.60,1.60,7,4,Intel Smart Cache,Intel UHD 617 Graphics
Core i5-8257U,Launched,Q3'19,4,8,14,3.90,1.40,15,6,Intel Smart Cache,Intel Iris Plus Graphics 645
Core i5-8279U,Launched,Q2'19,4,8,14,4.10,2.40,28,6,Intel Smart Cache,Intel Iris Plus Graphics 655
Core i5-8365U,Launched,Q2'19,4,8,14,4.10,1.60,15,6,Intel Smart Cache,Intel UHD Graphics for 8th Generation Intel Core Processors
Core i5-8365UE,Launched,Q2'19,4,8,14,4.10,1.60,15,6,Intel Smart Cache,Intel UHD 620 Graphics
Core i5-8310Y,Launched,Q1'19,2,4,14,3.90,1.60,7,4,Intel Smart Cache,Intel UHD 617 Graphics
Core i5-8260U,Launched,Q4'19,4,8,14,3.90,1.60,15,6,Intel Smart Cache,Intel UHD 620 Graphics
Core i5-7200U,Launched,Q3'16,2,4,14,3.10,2.50,15,3,Intel Smart Cache,Intel HD 620 Graphics
Core i5-7Y54,Launched,Q3'16,2,4,14,3.20,1.20,4.5,4,Intel Smart Cache,Intel HD 615 Graphics
Core i5-7500T,Launched,Q1'17,4,4,14,3.30,2.70,35,6,Intel Smart Cache,Intel HD 630 Graphics
Core i5-7500,Launched,Q1'17,4,4,14,3.80,3.40,65,6,Intel Smart Cache,Intel HD 630 Graphics
Core i5-7600K,Discontinued,Q1'17,4,4,14,4.20,3.80,91,6,Intel Smart Cache,Intel HD 630 Graphics
Core i5-7400,Discontinued,Q1'17,4,4,14,3.50,3.00,65,6,Intel Smart Cache,Intel HD 630 Graphics
Core i5-7600,Discontinued,Q1'17,4,4,14,4.10,3.50,65,6,Intel Smart Cache,Intel HD 630 Graphics
Core i5-7600T,Discontinued,Q1'17,4,4,14,3.70,2.80,35,6,Intel Smart Cache,Intel HD 630 Graphics
Core i5-7400T,Discontinued,Q1'17,4,4,14,3.00,2.40,35,6,Intel Smart Cache,Intel HD 630 Graphics
Core i5-7300HQ,Launched,Q1'17,4,4,14,3.50,2.50,45,6,N/A,Intel HD 630 Graphics
Core i5-7440HQ,Launched,Q1'17,4,4,14,3.80,2.80,45,6,N/A,Intel HD 630 Graphics
Core i5-7Y57,Launched,Q1'17,2,4,14,3.30,1.20,4.5,4,Intel Smart Cache,Intel HD 615 Graphics
Core i5-7300U,Launched,Q1'17,2,4,14,3.50,2.60,15,3,Intel Smart Cache,Intel HD 620 Graphics
Core i5-7440EQ,Launched,Q1'17,4,4,14,3.60,2.90,45,6,N/A,Intel HD 630 Graphics
Core i5-7267U,Discontinued,Q1'17,2,4,14,3.50,3.10,28,4,N/A,Intel Iris Plus 650 Graphics
Core i5-7287U,Discontinued,Q1'17,2,4,14,3.70,3.30,28,4,N/A,Intel Iris Plus 650 Graphics
Core i5-7442EQ,Launched,Q1'17,4,4,14,2.90,2.10,25,6,N/A,Intel HD 630 Graphics
Core i5-7360U,Launched,Q1'17,2,4,14,3.60,2.30,15,4,N/A,Intel Iris Plus 640 Graphics
Core i5-7260U,Launched,Q1'17,2,4,14,3.40,2.20,15,4,N/A,Intel Iris Plus 640 Graphics
Core i5-6500T,Discontinued,Q3'15,4,4,14,3.10,2.50,35,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6500,Launched,Q3'15,4,4,14,3.60,3.20,65,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6400,Discontinued,Q3'15,4,4,14,3.30,2.70,65,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6500TE,Launched,Q4'15,4,4,14,3.30,2.30,35,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6400T,Discontinued,Q3'15,4,4,14,2.80,2.20,35,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6600,Discontinued,Q3'15,4,4,14,3.90,3.30,65,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6600T,Discontinued,Q3'15,4,4,14,3.50,2.70,35,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6300U,Launched,Q3'15,2,4,14,3.00,2.40,15,3,Intel Smart Cache,Intel HD 520 Graphics
Core i5-6600K,Discontinued,Q3'15,4,4,14,3.90,3.50,91,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6200U,Discontinued,Q3'15,2,4,14,2.80,2.30,15,3,Intel Smart Cache,Intel HD 520 Graphics
Core i5-6300HQ,Discontinued,Q3'15,4,4,14,3.20,2.30,45,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6440HQ,Discontinued,Q3'15,4,4,14,3.50,2.60,45,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6440EQ,Launched,Q4'15,4,4,14,3.40,2.70,45,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6442EQ,Launched,Q4'15,4,4,14,2.70,1.90,25,6,Intel Smart Cache,Intel HD 530 Graphics
Core i5-6360U,Discontinued,Q3'15,2,4,14,3.10,2.00,15,4,Intel Smart Cache,Intel Iris 540 Graphics
Core i5-6260U,Discontinued,Q3'15,2,4,14,2.90,1.80,15,4,Intel Smart Cache,Intel Iris 540 Graphics
Core i5-6287U,Discontinued,Q3'15,2,4,14,3.50,3.10,28,4,Intel Smart Cache,Intel Iris 550 Graphics
Core i5-6267U,Launched,Q3'15,2,4,14,3.30,2.90,28,4,Intel Smart Cache,Intel Iris 550 Graphics
Core i5-6402P,Discontinued,Q4'15,4,4,14,3.40,2.80,65,6,N/A,Intel HD 510 Graphics
Core i5-6350HQ,Discontinued,Q1'16,4,4,14,3.20,2.30,45,6,Intel Smart Cache,Intel Iris Pro 580 Graphics
Core i5-6585R,Discontinued,Q2'16,4,4,14,3.60,2.80,65,6,N/A,Intel Iris Pro 580 Graphics
Core i5-6685R,Discontinued,Q2'16,4,4,14,3.80,3.20,65,6,N/A,Intel Iris Pro 580 Graphics
Core i5-5250U,Discontinued,Q1'15,2,4,14,2.70,1.60,15,3,N/A,Intel HD 6000 Graphics
Core i5-5257U,Launched,Q1'15,2,4,14,3.10,2.70,28,3,N/A,Intel Iris 6100 Graphics
Core i5-5287U,Discontinued,Q1'15,2,4,14,3.30,2.90,28,3,N/A,Intel Iris 6100 Graphics
Core i5-5350U,Launched,Q1'15,2,4,14,2.90,1.80,15,3,N/A,Intel HD 6000 Graphics
Core i5-5200U,Discontinued,Q1'15,2,4,14,2.70,2.20,15,3,N/A,Intel HD 5500 Graphics
Core i5-5300U,Discontinued,Q1'15,2,4,14,2.90,2.30,15,3,N/A,Intel HD 5500 Graphics
Core i5-5350H,Discontinued,Q2'15,2,4,14,3.50,3.10,47,4,N/A,Intel Iris Pro 6200 Graphics
Core i5-5575R,Discontinued,Q2'15,4,4,14,3.30,2.80,65,4,N/A,Intel Iris Pro 6200 Graphics
Core i5-5675R,Discontinued,Q2'15,4,4,14,3.60,3.10,65,4,N/A,Intel Iris Pro 6200 Graphics
Core i5-5675C,Discontinued,Q2'15,4,4,14,3.60,3.10,65,4,N/A,Intel Iris Pro 6200 Graphics
Core i5-4200H,Discontinued,Q4'13,2,4,22,3.40,2.80,47,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4250U,Discontinued,Q3'13,2,4,22,2.60,1.30,15,3,Intel Smart Cache,Intel HD 5000 Graphics
Core i5-4260U,Discontinued,Q2'14,2,4,22,2.70,1.40,15,3,Intel Smart Cache,Intel HD 5000 Graphics
Core i5-4350U,Discontinued,Q3'13,2,4,22,2.90,1.40,15,3,Intel Smart Cache,Intel HD 5000 Graphics
Core i5-4360U,Discontinued,Q1'14,2,4,22,3.00,1.50,15,3,Intel Smart Cache,Intel HD 5000 Graphics
Core i5-4430,Discontinued,Q2'13,4,4,22,3.20,3.00,84,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4430S,Discontinued,Q2'13,4,4,22,3.20,2.70,65,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4440,Discontinued,Q3'13,4,4,22,3.30,3.10,84,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4440S,Discontinued,Q3'13,4,4,22,3.30,2.80,65,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4570,Discontinued,Q2'13,4,4,22,3.60,3.20,84,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4570S,Launched,Q2'13,4,4,22,3.60,2.90,65,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4570T,Discontinued,Q2'13,2,4,22,3.60,2.90,35,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4670,Discontinued,Q2'13,4,4,22,3.80,3.40,84,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4670K,Discontinued,Q2'13,4,4,22,3.80,3.40,84,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4670S,Discontinued,Q2'13,4,4,22,3.80,3.10,65,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4670T,Discontinued,Q2'13,4,4,22,3.30,2.30,45,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4200U,Discontinued,Q3'13,2,4,22,2.60,1.60,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i5-4570TE,Launched,Q2'13,2,4,22,3.30,2.70,35,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4402EC,Launched,Q1'14,2,4,22,N/A,2.50,27,4,Intel Smart Cache,N/A
Core i5-4200Y,Discontinued,Q3'13,2,4,22,1.90,1.40,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i5-4258U,Discontinued,Q3'13,2,4,22,2.90,2.40,28,3,Intel Smart Cache,Intel Iris 5100 Graphics
Core i5-4288U,Discontinued,Q3'13,2,4,22,3.10,2.60,28,3,Intel Smart Cache,Intel Iris 5100 Graphics
Core i5-4400E,Launched,Q3'13,2,4,22,3.30,2.70,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4402E,Launched,Q3'13,2,4,22,2.70,1.60,25,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4300U,Launched,Q3'13,2,4,22,2.90,1.90,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i5-4300M,Discontinued,Q4'13,2,4,22,3.30,2.60,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4200M,Discontinued,Q4'13,2,4,22,3.10,2.50,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4202Y,Discontinued,Q3'13,2,4,22,2.00,1.60,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i5-4210Y,Discontinued,Q3'13,2,4,22,1.90,1.50,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i5-4300Y,Discontinued,Q3'13,2,4,22,2.30,1.60,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i5-4302Y,Discontinued,Q3'13,2,4,22,2.30,1.60,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i5-4570R,Discontinued,Q2'13,4,4,22,3.20,2.70,65,4,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i5-4670R,Discontinued,Q2'13,4,4,22,3.70,3.00,65,4,Intel Smart Cache,Intel Iris Pro 5200 Graphics
Core i5-4330M,Discontinued,Q4'13,2,4,22,3.50,2.80,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4460T,Discontinued,Q2'14,4,4,22,2.70,1.90,35,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4590T,Launched,Q2'14,4,4,22,3.00,2.00,35,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4210H,Discontinued,Q3'14,2,4,22,3.50,2.90,47,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4410E,Launched,Q2'14,2,4,22,N/A,2.90,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4422E,Launched,Q2'14,2,4,22,2.90,1.80,25,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4310U,Discontinued,Q1'14,2,4,22,3.00,2.00,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i5-4340M,Discontinued,Q1'14,2,4,22,3.60,2.90,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4310M,Discontinued,Q1'14,2,4,22,3.40,2.70,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4690,Discontinued,Q2'14,4,4,22,3.90,3.50,84,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4690K,Discontinued,Q2'14,4,4,22,3.90,3.50,88,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4690S,Discontinued,Q2'14,4,4,22,3.90,3.20,65,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4690T,Discontinued,Q2'14,4,4,22,3.50,2.50,45,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4590,Discontinued,Q2'14,4,4,22,3.70,3.30,84,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4590S,Launched,Q2'14,4,4,22,3.70,3.00,65,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4460,Discontinued,Q2'14,4,4,22,3.40,3.20,84,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4460S,Discontinued,Q2'14,4,4,22,3.40,2.90,65,6,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4210M,Discontinued,Q2'14,2,4,22,3.20,2.60,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i5-4210U,Discontinued,Q2'14,2,4,22,2.70,1.70,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i5-4220Y,Discontinued,Q2'14,2,4,22,2.00,1.60,11.5,3,N/A,Intel HD 4200 Graphics
Core i5-4308U,Discontinued,Q3'14,2,4,22,3.30,2.80,28,3,N/A,Intel Iris 5100 Graphics
Core i5-4278U,Discontinued,Q3'14,2,4,22,3.10,2.60,28,3,N/A,Intel Iris 5100 Graphics
Core i3-1115GRE,Launched,Q3'20,2,4,10,3.90,2.20,15,6,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-1115G4E,Launched,Q3'20,2,4,10,3.90,2.20,15,6,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-1110G4,Launched,Q3'20,2,4,10,3.90,N/A,N/A,6,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-1115G4,Launched,Q3'20,2,4,10,4.10,N/A,N/A,6,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-1125G4,Launched,Q1'21,4,8,10,3.70,N/A,N/A,8,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-1115G4 (with IPU),Launched,Q3'20,2,4,10,4.10,N/A,N/A,6,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-1125G4 (with IPU),Launched,Q1'21,4,8,10,3.70,N/A,N/A,8,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-1120G4,Launched,Q1'21,4,8,10,3.50,N/A,N/A,8,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-11100HE,Launched,Q3'21,4,8,10,4.40,N/A,N/A,8,Intel Smart Cache,Intel UHD Graphics for 11th Gen Intel Core Processors
Core i3-10110U,Launched,Q3'19,2,4,14,4.10,2.10,15,4,Intel Smart Cache,Intel UHD Graphics for 10th Gen Intel Core Processors
Core i3-10110Y,Launched,Q3'19,2,4,14,4.00,1.00,7,4,Intel Smart Cache,Intel UHD Graphics for 10th Gen Intel Core Processors
Core i3-1005G1,Launched,Q3'19,2,4,10,3.40,1.20,15,4,Intel Smart Cache,Intel UHD Graphics for 10th Gen Intel Core Processors
Core i3-1000G1,Launched,Q3'19,2,4,10,3.20,1.10,9,4,Intel Smart Cache,Intel UHD Graphics for 10th Gen Intel Core Processors
Core i3-1000G4,Launched,Q3'19,2,4,10,3.20,1.10,9,4,Intel Smart Cache,Intel Iris Plus Graphics
Core i3-10320,Launched,Q2'20,4,8,14,4.60,3.80,65,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10300,Launched,Q2'20,4,8,14,4.40,3.70,65,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10300T,Launched,Q2'20,4,8,14,3.90,3.00,35,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10100,Launched,Q2'20,4,8,14,4.30,3.60,65,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10100T,Launched,Q2'20,4,8,14,3.80,3.00,35,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10325,Launched,Q1'21,4,8,14,4.70,3.90,65,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10105T,Launched,Q1'21,4,8,14,3.90,3.00,35,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10305,Launched,Q1'21,4,8,14,4.50,3.80,65,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10105,Launched,Q1'21,4,8,14,4.40,3.70,65,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10305T,Launched,Q1'21,4,8,14,4.00,3.00,35,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10100F,Launched,Q4'20,4,8,14,4.30,3.60,65,6,Intel Smart Cache,N/A
Core i3-10105F,Launched,Q1'21,4,8,14,4.40,3.70,65,6,Intel Smart Cache,N/A
Core i3-10100E,Launched,Q2'20,4,8,14,3.80,3.20,65,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10100TE,Launched,Q2'20,4,8,14,3.60,2.30,35,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-10100Y,Launched,Q1'21,2,4,14,3.90,1.30,5,4,Intel Smart Cache,Intel UHD 615 Graphics
Core i3-9100,Launched,Q2'19,4,4,14,4.20,3.60,65,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-9100T,Launched,Q2'19,4,4,14,3.70,3.10,35,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-9300T,Launched,Q2'19,4,4,14,3.80,3.20,35,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-9300,Launched,Q2'19,4,4,14,4.30,3.70,62,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-9350K,Launched,Q2'19,4,4,14,4.60,4.00,91,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-9100F,Launched,Q2'19,4,4,14,4.20,3.60,65,6,Intel Smart Cache,N/A
Core i3-9350KF,Launched,Q1'19,4,4,14,4.60,4.00,91,8,Intel Smart Cache,N/A
Core i3-9320,Launched,Q2'19,4,4,14,4.40,3.70,62,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-9100E,Launched,Q2'19,4,4,14,3.70,3.10,65,6,N/A,Intel UHD 630 Graphics
Core i3-9100HL,Launched,Q2'19,4,4,14,2.90,1.60,25,6,N/A,Intel UHD 630 Graphics
Core i3-9100TE,Launched,Q2'19,4,4,14,3.20,2.20,35,6,N/A,Intel UHD 630 Graphics
Core i3-8100,Launched,Q4'17,4,4,14,N/A,3.60,65,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-8350,Discontinued,Q4'17,4,4,14,N/A,4.00,91,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-8300,Discontinued,Q2'18,4,4,14,N/A,3.70,62,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-8300T,Discontinued,Q2'18,4,4,14,N/A,3.20,35,8,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-8100T,Launched,Q2'18,4,4,14,N/A,3.10,35,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-8109U,Launched,Q2'18,2,4,14,3.60,3.00,28,4,Intel Smart Cache,Intel Iris Plus Graphics 655
Core i3-8130U,Launched,Q1'18,2,4,14,3.40,2.20,15,4,Intel Smart Cache,Intel UHD 620 Graphics
Core i3-8145U,Launched,Q3'18,2,4,14,3.90,2.10,15,4,Intel Smart Cache,Intel UHD Graphics for 8th Gen Intel Processors
Core i3-8100H,Launched,Q3'18,4,4,14,N/A,3.00,45,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-8100B,Launched,Q3'18,4,4,14,N/A,3.60,65,6,Intel Smart Cache,Intel UHD 630 Graphics
Core i3-8145UE,Launched,Q2'19,2,4,14,3.90,2.20,15,4,Intel Smart Cache,Intel UHD 620 Graphics
Core i3-8140U,Launched,Q4'19,2,4,14,3.90,2.10,15,4,Intel Smart Cache,Intel UHD 620 Graphics
Core i3-7020U,Launched,Q2'18,2,4,14,N/A,2.30,15,3,Intel Smart Cache,Intel HD 620 Graphics
Core i3-7130U,Launched,Q2'17,2,4,14,N/A,2.70,15,3,Intel Smart Cache,Intel HD 620 Graphics
Core i3-7100U,Launched,Q3'16,2,4,14,N/A,2.40,15,3,Intel Smart Cache,Intel HD 620 Graphics
Core i3-7102E,Launched,Q1'17,2,4,14,N/A,2.10,25,3,N/A,Intel HD 630 Graphics
Core i3-7101TE,Launched,Q1'17,2,4,14,N/A,3.40,35,3,Intel Smart Cache,Intel HD 630 Graphics
Core i3-7100H,Launched,Q1'17,2,4,14,N/A,3.00,35,3,N/A,Intel HD 630 Graphics
Core i3-7101E,Launched,Q1'17,2,4,14,N/A,3.90,54,3,Intel Smart Cache,Intel HD 630 Graphics
Core i3-7100E,Launched,Q1'17,2,4,14,N/A,2.90,35,3,N/A,Intel HD 630 Graphics
Core i3-7100,Discontinued,Q1'17,2,4,14,N/A,3.90,51,3,Intel Smart Cache,Intel HD 630 Graphics
Core i3-7300T,Discontinued,Q1'17,2,4,14,N/A,3.50,35,4,Intel Smart Cache,Intel HD 630 Graphics
Core i3-7300,Discontinued,Q1'17,2,4,14,N/A,4.00,51,4,Intel Smart Cache,Intel HD 630 Graphics
Core i3-7320,Discontinued,Q1'17,2,4,14,N/A,4.10,51,4,Intel Smart Cache,Intel HD 630 Graphics
Core i3-7100T,Discontinued,Q1'17,2,4,14,N/A,3.40,35,3,Intel Smart Cache,Intel HD 630 Graphics
Core i3-7350K,Discontinued,Q1'17,2,4,14,N/A,4.20,60,4,Intel Smart Cache,Intel HD 630 Graphics
Core i3-7167U,Launched,Q1'17,2,4,14,N/A,2.80,28,3,N/A,Intel Iris Plus 650 Graphics
Core i3-6100U,Launched,Q3'15,2,4,14,N/A,2.30,15,3,Intel Smart Cache,Intel HD 520 Graphics
Core i3-6100TE,Launched,Q4'15,2,4,14,N/A,2.70,35,4,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6100H,Discontinued,Q3'15,2,4,14,N/A,2.70,35,3,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6100E,Launched,Q4'15,2,4,14,N/A,2.70,35,3,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6102E,Launched,Q4'15,2,4,14,N/A,1.90,25,3,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6300T,Discontinued,Q3'15,2,4,14,N/A,3.30,35,4,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6100,Launched,Q3'15,2,4,14,N/A,3.70,51,3,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6300,Discontinued,Q3'15,2,4,14,N/A,3.80,51,4,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6320,Discontinued,Q3'15,2,4,14,N/A,3.90,51,4,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6100T,Discontinued,Q3'15,2,4,14,N/A,3.20,35,3,Intel Smart Cache,Intel HD 530 Graphics
Core i3-6167U,Discontinued,Q3'15,2,4,14,N/A,2.70,28,3,Intel Smart Cache,Intel Iris 550 Graphics
Core i3-6006U,Discontinued,Q4'16,2,4,14,N/A,2.00,15,3,Intel Smart Cache,Intel HD 520 Graphics
Core i3-6098P,Discontinued,Q4'15,2,4,14,N/A,3.60,54,3,N/A,Intel HD 510 Graphics
Core i3-6157U,Discontinued,Q3'16,2,4,14,N/A,2.40,28,3,Intel Smart Cache,Intel Iris 550 Graphics
Core i3-5005U,Launched,Q1'15,2,4,14,N/A,2.00,15,3,N/A,Intel HD 5500 Graphics
Core i3-5010U,Launched,Q1'15,2,4,14,N/A,2.10,15,3,N/A,Intel HD 5500 Graphics
Core i3-5015U,Discontinued,Q1'15,2,4,14,N/A,2.10,15,3,N/A,Intel HD 5500 Graphics
Core i3-5020U,Discontinued,Q1'15,2,4,14,N/A,2.20,15,3,N/A,Intel HD 5500 Graphics
Core i3-5157U,Discontinued,Q1'15,2,4,14,N/A,2.50,28,3,N/A,Intel Iris 6100 Graphics
Core i3-4000M,Discontinued,Q4'13,2,4,22,N/A,2.40,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4005M,Discontinued,Q3'13,2,4,22,N/A,1.70,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4010U,Launched,Q3'13,2,4,22,N/A,1.70,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4100U,Discontinued,Q3'13,2,4,22,N/A,1.80,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4010Y,Discontinued,Q3'13,2,4,22,N/A,1.30,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i3-4158U,Discontinued,Q3'13,2,4,22,N/A,2.00,28,3,Intel Smart Cache,Intel Iris 5100 Graphics
Core i3-4100E,Launched,Q3'13,2,4,22,N/A,2.40,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4102E,Launched,Q3'13,2,4,22,N/A,1.60,25,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4100M,Discontinued,Q4'13,2,4,22,N/A,2.50,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4012Y,Discontinued,Q3'13,2,4,22,N/A,1.50,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i3-4020Y,Discontinued,Q3'13,2,4,22,N/A,1.50,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i3-4130,Discontinued,Q3'13,2,4,22,N/A,3.40,54,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4130T,Discontinued,Q3'13,2,4,22,N/A,2.90,35,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4110M,Discontinued,Q2'14,2,4,22,N/A,2.60,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4150,Discontinued,Q2'14,2,4,22,N/A,3.50,54,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4150T,Discontinued,Q2'14,2,4,22,N/A,3.00,35,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4160,Discontinued,Q3'14,2,4,22,N/A,3.60,54,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4160T,Discontinued,Q3'14,2,4,22,N/A,3.10,35,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4170,Discontinued,Q1'15,2,4,22,N/A,3.70,54,3,N/A,Intel HD 4400 Graphics
Core i3-4350,Discontinued,Q2'14,2,4,22,N/A,3.60,54,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4350T,Launched,Q2'14,2,4,22,N/A,3.10,35,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4360,Launched,Q2'14,2,4,22,N/A,3.70,54,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4360T,Discontinued,Q3'14,2,4,22,N/A,3.20,35,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4370,Discontinued,Q3'14,2,4,22,N/A,3.80,54,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4330,Launched,Q3'13,2,4,22,N/A,3.50,54,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4330T,Discontinued,Q3'13,2,4,22,N/A,3.00,35,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4340,Discontinued,Q3'13,2,4,22,N/A,3.60,54,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4330TE,Launched,Q3'13,2,4,22,N/A,2.40,35,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4110E,Launched,Q2'14,2,4,22,N/A,2.60,37,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4112E,Launched,Q2'14,2,4,22,N/A,1.80,25,3,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4340TE,Launched,Q2'14,2,4,22,N/A,2.60,35,4,Intel Smart Cache,Intel HD 4600 Graphics
Core i3-4120U,Discontinued,Q2'14,2,4,22,N/A,2.00,15,3,N/A,Intel HD 4400 Graphics
Core i3-4030U,Discontinued,Q2'14,2,4,22,N/A,1.90,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4025U,Discontinued,Q2'14,2,4,22,N/A,1.90,15,3,Intel Smart Cache,Intel HD 4400 Graphics
Core i3-4030Y,Discontinued,Q2'14,2,4,22,N/A,1.60,11.5,3,Intel Smart Cache,Intel HD 4200 Graphics
Core i3-4370T,Discontinued,Q1'15,2,4,22,N/A,3.30,35,4,N/A,Intel HD 4600 Graphics
Core i3-4170T,Discontinued,Q1'15,2,4,22,N/A,3.20,35,3,N/A,Intel HD 4400 Graphics
Core m3-8100Y,Launched,Q3'18,2,4,14,3.40,1.10,5,4,Intel Smart Cache,Intel UHD 615 Graphics
Core m3-7Y30,Launched,Q3'16,2,4,14,2.60,1.00,4.5,4,Intel Smart Cache,Intel HD 615 Graphics
Core m3-7Y32,Launched,Q2'17,2,4,14,3.00,1.10,4.5,4,Intel Smart Cache,Intel HD 615 Graphics
Core m5-6Y57,Discontinued,Q3'15,2,4,14,2.80,1.10,4.5,4,Intel Smart Cache,Intel HD 515 Graphics
Core m3-6Y30,Discontinued,Q3'15,2,4,14,2.20,0.90,4.5,4,Intel Smart Cache,Intel HD 515 Graphics
Core m7-6Y75,Discontinued,Q3'15,2,4,14,3.10,1.20,4.5,4,Intel Smart Cache,Intel HD 515 Graphics
Core m5-6Y54,Discontinued,Q3'15,2,4,14,2.70,1.10,4.5,4,Intel Smart Cache,Intel HD 515 Graphics
Core M-5Y10,Discontinued,Q3'14,2,4,14,2.00,0.80,4.5,4,N/A,Intel HD 5300 Graphics
Core M-5Y10a,Discontinued,Q3'14,2,4,14,2.00,0.80,4.5,4,N/A,Intel HD 5300 Graphics
Core M-5Y70,Discontinued,Q3'14,2,4,14,2.60,1.10,4.5,4,N/A,Intel HD 5300 Graphics
Core M-5Y31,Discontinued,Q4'14,2,4,14,2.40,0.90,4.5,4,N/A,Intel HD 5300 Graphics
Core M-5Y51,Discontinued,Q4'14,2,4,14,2.60,1.10,4.5,4,N/A,Intel HD 5300 Graphics
Core M-5Y71,Discontinued,Q4'14,2,4,14,2.90,1.20,4.5,4,N/A,Intel HD 5300 Graphics
Core M-5Y10c,Discontinued,Q4'14,2,4,14,2.00,0.80,4.5,4,N/A,Intel HD 5300 Graphics
Core Duo L2300,Discontinued,N/A,2,N/A,65,N/A,1.50,15,2,L2 Cache,N/A
Core Duo L2400,Discontinued,Q1'06,2,N/A,65,N/A,1.66,15,2,L2 Cache,N/A
Core Duo L2500,Discontinued,N/A,2,N/A,65,N/A,1.83,15,2,L2 Cache,N/A
Core Duo T2050,Discontinued,N/A,2,N/A,65,N/A,1.60,31,2,L2 Cache,N/A
Core Duo T2250,Discontinued,N/A,2,N/A,65,N/A,1.73,31,2,L2 Cache,N/A
Core Duo T2300,Discontinued,N/A,2,2,65,N/A,1.66,31,2,L2 Cache,N/A
Core Duo T2300E,Discontinued,N/A,2,2,65,N/A,1.66,31,2,L2 Cache,N/A
Core Duo T2400,Discontinued,N/A,2,2,65,N/A,1.83,31,2,L2 Cache,N/A
Core Duo T2500,Discontinued,Q1'06,2,2,65,N/A,2.00,31,2,L2 Cache,N/A
Core Duo T2600,Discontinued,N/A,2,2,65,N/A,2.16,31,2,L2 Cache,N/A
Core Duo T2700,Discontinued,N/A,2,2,65,N/A,2.33,31,2,L2 Cache,N/A
Core Duo U2400,Discontinued,N/A,2,2,65,N/A,1.06,9,2,L2 Cache,N/A
Core Duo U2500,Discontinued,Q1'06,2,2,65,N/A,1.20,9,2,L2 Cache,N/A
Core Solo T1300,Discontinued,N/A,1,1,65,N/A,1.66,27,2,L2 Cache,N/A
Core Solo T1350,Discontinued,N/A,1,1,65,N/A,1.86,31,2,L2 Cache,N/A
Core Solo T1400,Discontinued,N/A,1,1,65,N/A,1.83,27,2,L2 Cache,N/A
Core Solo U1300,Discontinued,N/A,1,1,65,N/A,1.06,6,2,L2 Cache,N/A
Core Solo U1400,Discontinued,N/A,1,1,65,N/A,1.20,6,2,L2 Cache,N/A
Core2 Duo E6300,Discontinued,Q3'06,2,2,65,N/A,1.86,65,2,L2 Cache,N/A
Core2 Duo E6400,Discontinued,Q3'06,2,2,65,N/A,2.13,65,2,L2 Cache,N/A
Core2 Duo E6600,Discontinued,Q3'06,2,2,65,N/A,2.40,65,4,L2 Cache,N/A
Core2 Duo E6700,Discontinued,Q3'06,2,2,65,N/A,2.66,65,4,L2 Cache,N/A
Core2 Duo T5200,Discontinued,N/A,2,2,65,N/A,1.60,34,2,L2 Cache,N/A
Core2 Duo T5500,Discontinued,N/A,2,2,65,N/A,1.66,34,2,L2 Cache,N/A
Core2 Duo T5600,Discontinued,N/A,2,2,65,N/A,1.83,34,2,L2 Cache,N/A
Core2 Duo T7200,Discontinued,N/A,2,2,65,N/A,2.00,34,4,L2 Cache,N/A
Core2 Duo T7400,Discontinued,Q3'06,2,N/A,65,N/A,2.16,34,4,L2 Cache,N/A
Core2 Duo T7600,Discontinued,Q3'07,2,2,65,N/A,2.33,34,4,L2 Cache,N/A
Core2 X6800 Extreme,Discontinued,Q3'06,2,2,65,N/A,2.93,75,4,L2 Cache,N/A
Core Solo U1500,Discontinued,N/A,1,1,65,N/A,1.33,5.5,2,L2 Cache,N/A
Core2 Duo E4300,Discontinued,Q3'06,2,2,65,N/A,1.80,65,2,L2 Cache,N/A
Core2 Duo L7200,Discontinued,Q1'07,2,2,65,N/A,1.33,17,4,L2 Cache,N/A
Core2 Duo L7400,Discontinued,Q3'06,2,2,65,N/A,1.50,17,4,L2 Cache,N/A
Core2 QX6700 Extreme,Discontinued,Q4'06,4,4,65,N/A,2.66,130,8,L2 Cache,N/A
Core Duo T2350,Discontinued,N/A,2,2,65,N/A,1.86,31,2,L2 Cache,N/A
Core Duo T2450,Discontinued,N/A,2,2,65,N/A,2.00,31,2,L2 Cache,N/A
Core2 Duo E4400,Discontinued,Q2'07,2,2,65,N/A,2.00,65,2,L2 Cache,N/A
Core2 Duo E6320,Discontinued,Q2'07,2,2,65,N/A,1.86,65,4,L2 Cache,N/A
Core2 Duo E6420,Discontinued,Q2'07,2,2,65,N/A,2.13,65,4,L2 Cache,N/A
Core2 Duo L7300,Discontinued,Q2'07,2,2,65,N/A,1.40,17,4,L2 Cache,N/A
Core2 Duo L7500,Discontinued,Q3'06,2,2,65,N/A,1.60,17,4,L2 Cache,N/A
Core2 Duo T5300,Discontinued,N/A,2,2,65,N/A,1.73,34,2,L2 Cache,N/A
Core2 Duo T7100,Discontinued,Q2'07,2,2,65,N/A,1.80,35,2,L2 Cache,N/A
Core2 Duo T7300,Discontinued,Q2'07,2,2,65,N/A,2.00,35,4,L2 Cache,N/A
Core2 Duo T7500,Discontinued,Q3'06,2,2,65,N/A,2.20,35,4,L2 Cache,N/A
Core2 Duo T7700,Discontinued,Q2'07,2,2,65,N/A,2.40,35,4,L2 Cache,N/A
Core2 Duo U7500,Discontinued,Q3'06,2,2,65,N/A,1.06,10,2,L2 Cache,N/A
Core2 Duo U7600,Discontinued,Q2'07,2,2,65,N/A,1.20,10,2,L2 Cache,N/A
Core2 Quad Q6600,Discontinued,Q1'07,4,4,65,N/A,2.40,105,8,L2 Cache,N/A
Core2 QX6800 Extreme,Discontinued,Q2'07,4,4,65,N/A,2.93,130,8,L2 Cache,N/A
Core2 Duo E4500,Discontinued,Q3'07,2,2,65,N/A,2.20,65,2,L2 Cache,N/A
Core2 Duo E6540,Discontinued,Q3'07,2,2,65,N/A,2.33,65,4,L2 Cache,N/A
Core2 Duo E6550,Discontinued,Q3'07,2,2,65,N/A,2.33,65,4,L2 Cache,N/A
Core2 Duo E6750,Discontinued,Q3'07,2,2,65,N/A,2.66,65,4,L2 Cache,N/A
Core2 Duo E6850,Discontinued,Q3'07,2,2,65,N/A,3.00,65,4,L2 Cache,N/A
Core2 Duo T5250,Discontinued,N/A,2,2,65,N/A,1.50,35,2,L2 Cache,N/A
Core2 Duo T5450,Discontinued,N/A,2,2,65,N/A,1.66,35,2,L2 Cache,N/A
Core2 X7800 Extreme,Discontinued,Q3'07,2,2,65,N/A,2.60,44,4,L2 Cache,N/A
Core2 QX6850 Extreme,Discontinued,Q3'07,4,4,65,N/A,3.00,130,8,L2 Cache,N/A
Core2 Quad Q6700,Discontinued,Q3'07,4,4,65,N/A,2.66,105,8,L2 Cache,N/A
Core2 Duo T7250,Discontinued,Q3'07,2,2,65,N/A,2.00,35,2,L2 Cache,N/A
Core2 Duo T7800,Discontinued,Q3'07,2,2,65,N/A,2.60,35,4,L2 Cache,N/A
Core2 X7900 Extreme,Discontinued,Q3'07,2,2,65,N/A,2.80,44,4,L2 Cache,N/A
Core2 Duo T5470,Discontinued,N/A,2,2,65,N/A,1.60,35,2,L2 Cache,N/A
Core2 Solo U2100,Discontinued,Q3'07,1,1,65,N/A,1.06,5.5,1,L2 Cache,N/A
Core2 Solo U2200,Discontinued,Q3'07,1,1,65,N/A,1.20,5.5,1,L2 Cache,N/A
Core2 Duo E4600,Discontinued,Q4'07,2,2,65,N/A,2.40,65,2,L2 Cache,N/A
Core2 Duo L7700,Discontinued,Q3'07,2,2,65,N/A,1.80,17,4,L2 Cache,N/A
Core2 Duo T5550,Discontinued,N/A,2,2,65,N/A,1.83,35,2,L2 Cache,N/A
Core2 Duo T5270,Discontinued,N/A,2,2,65,N/A,1.40,35,2,L2 Cache,N/A
Core2 Duo T8300,Discontinued,Q1'08,2,2,45,N/A,2.40,35,3,L2 Cache,N/A
Core2 Duo E8200,Discontinued,Q1'08,2,2,45,N/A,2.66,65,6,L2 Cache,N/A
Core2 Duo E8400,Discontinued,Q1'08,2,2,45,N/A,3.00,65,6,L2 Cache,N/A
Core2 Duo E8500,Discontinued,Q1'08,2,2,45,N/A,3.16,65,6,L2 Cache,N/A
Core2 Duo T5750,Discontinued,Q1'08,2,2,65,N/A,2.00,35,2,L2 Cache,N/A
Core2 Duo T8100,Discontinued,Q1'08,2,2,45,N/A,2.10,35,3,L2 Cache,N/A
Core2 Duo T9300,Discontinued,Q1'08,2,2,45,N/A,2.50,35,6,L2 Cache,N/A
Core2 Duo T9500,Discontinued,Q1'08,2,N/A,45,N/A,2.60,35,6,L2 Cache,N/A
Core2 Duo U7700,Discontinued,Q1'08,2,2,65,N/A,1.33,10,2,L2 Cache,N/A
Core2 QX9650 Extreme,Discontinued,Q4'07,4,4,45,N/A,3.00,130,12,L2 Cache,N/A
Core2 Quad Q9300,Discontinued,Q1'08,4,4,45,N/A,2.50,95,6,L2 Cache,N/A
Core2 Quad Q9450,Discontinued,Q1'08,4,4,45,N/A,2.66,95,12,L2 Cache,N/A
Core2 Quad Q9550,Discontinued,Q1'08,4,4,45,N/A,2.83,95,12,L2 Cache,N/A
Core2 Duo E4700,Discontinued,Q1'08,2,2,65,N/A,2.60,65,2,L2 Cache,N/A
Core2 Duo E8190,Discontinued,Q1'08,2,2,45,N/A,2.66,65,6,L2 Cache,N/A
Core2 X9000 Extreme,Discontinued,Q1'08,2,2,45,N/A,2.80,44,6,L2 Cache,N/A
Core2 QX9770 Extreme,Discontinued,Q1'08,4,4,45,N/A,3.20,136,12,L2 Cache,N/A
Core2 QX9775 Extreme,Discontinued,Q1'08,4,4,45,N/A,3.20,150,12,L2 Cache,N/A
Core2 Duo E8300,Discontinued,Q2'08,2,2,45,N/A,2.83,65,6,L2 Cache,N/A
Core2 Duo T5670,Discontinued,Q2'08,2,2,65,N/A,1.80,35,2,L2 Cache,N/A
Core2 Duo E7200,Discontinued,Q2'08,2,2,45,N/A,2.53,65,3,L2 Cache,N/A
Core2 Quad Q9400,Discontinued,Q3'08,4,4,45,N/A,2.66,95,6,L2 Cache,N/A
Core2 Quad Q9650,Discontinued,Q3'08,4,4,45,N/A,3.00,95,12,L2 Cache,N/A
Core2 X9100 Extreme,Discontinued,Q3'08,2,2,45,N/A,3.06,44,6,L2 Cache,N/A
Core2 Duo T9400,Discontinued,Q3'08,2,2,45,N/A,2.53,35,6,L2 Cache,N/A
Core2 Duo T9600,Discontinued,Q3'08,2,N/A,45,N/A,2.80,35,6,L2 Cache,N/A
Core2 Duo P9500,Discontinued,Q3'08,2,2,45,N/A,2.53,25,6,L2 Cache,N/A
Core2 Duo P8600,Discontinued,Q3'08,2,2,45,N/A,2.40,25,3,L2 Cache,N/A
Core2 Duo P8400,Discontinued,Q3'08,2,2,45,N/A,2.26,25,3,L2 Cache,N/A
Core2 Duo T5800,Discontinued,Q4'08,2,2,65,N/A,2.00,35,2,L2 Cache,N/A
Core2 Duo E8600,Discontinued,Q3'08,2,2,45,N/A,3.33,65,6,L2 Cache,N/A
Core2 Duo E7300,Discontinued,Q3'08,2,2,45,N/A,2.66,65,3,L2 Cache,N/A
Core2 Duo E7400,Discontinued,Q1'08,2,2,45,N/A,2.80,65,3,L2 Cache,N/A
Core2 Duo E7500,Discontinued,Q1'09,2,2,45,N/A,2.93,65,3,L2 Cache,N/A
Core2 Quad Q8200,Discontinued,Q3'08,4,4,45,N/A,2.33,95,4,L2 Cache,N/A
Core2 Duo SL9300,Discontinued,Q3'08,2,2,45,N/A,1.60,17,6,L2 Cache,N/A
Core2 Duo SL9400,Discontinued,Q3'08,2,2,45,N/A,1.86,17,6,L2 Cache,N/A
Core2 Duo SP9300,Discontinued,Q3'08,2,2,45,N/A,2.26,25,6,L2 Cache,N/A
Core2 Duo SP9400,Discontinued,Q3'08,2,2,45,N/A,2.40,25,6,L2 Cache,N/A
Core2 Duo SU9300,Discontinued,Q3'08,2,2,45,N/A,1.20,10,3,L2 Cache,N/A
Core2 Duo SU9400,Discontinued,Q3'08,2,2,45,N/A,1.40,10,3,L2 Cache,N/A
Core2 QX9300 Extreme,Discontinued,Q3'08,4,4,45,N/A,2.53,45,12,L2 Cache,N/A
Core2 Solo ULV SU3300,Discontinued,Q3'08,1,1,45,N/A,1.20,5.5,3,L2 Cache,N/A
Core2 Duo P7450,Discontinued,Q1'09,2,2,45,N/A,2.13,25,3,L2 Cache,N/A
Core2 Duo P7350,Discontinued,Q3'08,2,2,45,N/A,2.00,25,3,L2 Cache,N/A
Core2 Duo U7500,Discontinued,Q3'06,2,2,65,N/A,1.06,10,2,L2 Cache,N/A
Core2 Duo U7600,Discontinued,N/A,2,2,65,N/A,1.20,10,2,L2 Cache,N/A
Core2 Duo T9800,Discontinued,Q4'08,2,2,45,N/A,2.93,35,6,L2 Cache,N/A
Core2 Duo P8700,Discontinued,Q4'08,2,2,45,N/A,2.53,25,3,L2 Cache,N/A
Core2 Quad Q9100,Discontinued,Q3'08,4,4,45,N/A,2.26,45,12,L2 Cache,N/A
Core2 Duo T5870,Discontinued,N/A,2,2,65,N/A,2.00,35,2,L2 Cache,N/A
Core2 Duo P7370,Discontinued,Q4'08,2,2,45,N/A,2.00,25,3,L2 Cache,N/A
Core2 Duo T9550,Discontinued,Q4'08,2,2,45,N/A,2.66,35,6,L2 Cache,N/A
Core2 Solo ULV SU3500,Discontinued,Q2'09,1,1,45,N/A,1.40,5.5,3,L2 Cache,N/A
Core i7-920,Discontinued,Q4'08,4,4,45,2.93,2.66,130,8,Intel Smart Cache,N/A
Core i7-940,Discontinued,Q4'08,4,8,45,3.20,2.93,130,8,Intel Smart Cache,N/A
Core i7-965 Extreme Edition,Discontinued,Q4'08,4,8,45,3.46,3.20,130,8,Intel Smart Cache,N/A
Core i7-950,Discontinued,Q2'09,4,8,45,3.33,3.06,130,8,Intel Smart Cache,N/A
Core i7-960,Discontinued,Q4'09,4,8,45,3.46,3.20,130,8,Intel Smart Cache,N/A
Core i7-975 Extreme Edition,Discontinued,Q2'09,4,8,45,3.60,3.33,130,8,Intel Smart Cache,N/A
Core2 Quad Q9500,Discontinued,N/A,4,4,45,N/A,2.83,95,6,L2 Cache,N/A
Core2 Duo SL9380,Discontinued,Q3'08,2,2,45,N/A,1.80,17,6,L2 Cache,N/A
Core Solo T1250,Discontinued,N/A,1,N/A,65,N/A,1.73,31,2,L2 Cache,N/A
Core2 Duo T6600,Discontinued,Q1'09,2,2,45,N/A,2.20,35,2,L2 Cache,N/A
Core2 Duo SP9600,Discontinued,Q1'09,2,2,45,N/A,2.53,25,6,L2 Cache,N/A
Core2 Duo SL9600,Discontinued,Q1'09,2,2,45,N/A,2.13,17,6,L2 Cache,N/A
Core2 Duo SU9600,Discontinued,Q1'09,2,2,45,N/A,1.60,10,3,L2 Cache,N/A
Core2 Duo P9600,Discontinued,Q4'08,2,2,45,N/A,2.66,25,6,L2 Cache,N/A
Core2 Quad Q8400,Discontinued,Q2'09,4,4,45,N/A,2.66,95,4,L2 Cache,N/A
Core2 Quad Q8300,Discontinued,Q4'08,4,4,45,N/A,2.50,95,4,L2 Cache,N/A
Core2 Duo T6500,Discontinued,Q2'09,2,2,45,N/A,2.10,35,2,L2 Cache,N/A
Core2 Duo T9900,Discontinued,Q2'09,2,2,45,N/A,3.06,35,6,L2 Cache,N/A
Core2 Duo P8800,Discontinued,Q2'09,2,2,45,N/A,2.66,25,3,L2 Cache,N/A
Core2 Duo T6400,Discontinued,Q1'09,2,2,45,N/A,2.00,35,2,L2 Cache,N/A
Core2 Quad Q9000,Discontinued,Q1'09,4,4,45,N/A,2.00,45,6,L2 Cache,N/A
Core2 Quad Q9400S,Discontinued,Q1'09,4,4,45,N/A,2.66,65,6,L2 Cache,N/A
Core2 Quad Q9550S,Discontinued,Q1'09,4,4,45,N/A,2.83,65,12,L2 Cache,N/A
Core2 Quad Q8200S,Discontinued,Q1'09,4,4,45,N/A,2.33,65,4,L2 Cache,N/A
Core i7-870,Discontinued,Q3'09,4,8,45,3.60,2.93,95,8,Intel Smart Cache,N/A
Core i7-860,Discontinued,Q3'09,4,8,45,3.46,2.80,95,8,Intel Smart Cache,N/A
Core i7-860S,Discontinued,Q1'10,4,8,45,3.46,2.53,82,8,Intel Smart Cache,N/A
Core i7-930,Discontinued,Q1'10,4,8,45,3.06,2.80,130,8,Intel Smart Cache,N/A
Core2 Duo E7600,Discontinued,Q2'09,2,2,45,N/A,3.06,65,3,L2 Cache,N/A
Core2 Duo P7550,Discontinued,Q3'09,2,2,45,N/A,2.26,25,3,L2 Cache,N/A
Core2 Duo T6670,Discontinued,Q3'09,2,2,45,N/A,2.20,35,2,L2 Cache,N/A
Core2 Quad Q8400S,Discontinued,Q2'09,4,4,45,N/A,2.66,65,4,L2 Cache,N/A
Core2 Solo SU3500,Discontinued,Q2'09,1,1,45,N/A,1.30,5.5,3,N/A,N/A
Core2 Duo P7570,Discontinued,Q3'09,2,2,45,N/A,2.26,25,3,L2 Cache,N/A
Core2 Duo P9700,Discontinued,Q2'09,2,2,45,N/A,2.80,28,6,L2 Cache,N/A
Core i5-750,Discontinued,Q3'09,4,4,45,3.20,2.66,95,8,Intel Smart Cache,N/A
Core i5-750S,Discontinued,Q1'10,4,4,45,3.20,2.40,82,8,Intel Smart Cache,N/A
Core2 Quad Q9505,Discontinued,Q3'09,4,4,45,N/A,2.83,95,6,L2 Cache,N/A
Core2 Quad Q9505S,Discontinued,Q3'09,4,4,45,N/A,2.83,65,6,L2 Cache,N/A
Core i7-720QM,Discontinued,Q3'09,4,8,45,2.80,1.60,45,6,Intel Smart Cache,N/A
Core i7-820QM,Discontinued,Q3'09,4,8,45,3.06,1.73,45,8,Intel Smart Cache,N/A
Core i7-840QM,Discontinued,Q3'10,4,8,45,3.20,1.86,45,8,Intel Smart Cache,N/A
Core i7-920XM Extreme Edition,Discontinued,Q3'09,4,8,45,3.20,2.00,55,8,Intel Smart Cache,N/A
Core i7-940XM Extreme Edition,Discontinued,Q3'10,4,8,45,3.33,2.13,55,8,Intel Smart Cache,N/A
Core i3-350M,Discontinued,Q1'10,2,4,32,N/A,2.26,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-430M,Discontinued,Q1'10,2,4,32,2.53,2.26,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-540M,Discontinued,Q1'10,2,4,32,3.07,2.53,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-650,Discontinued,Q1'10,2,4,32,3.46,3.20,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-660,Discontinued,Q1'10,2,4,32,3.60,3.33,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-661,Discontinued,Q1'10,2,4,32,3.60,3.33,87,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-670,Discontinued,Q1'10,2,4,32,3.73,3.46,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-620LM,Discontinued,Q1'10,2,4,32,2.80,2.00,25,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-620M,Discontinued,Q1'10,2,4,32,3.33,2.66,35,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-620UM,Discontinued,Q1'10,2,4,32,2.13,1.06,18,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-640LM,Discontinued,Q1'10,2,4,32,2.93,2.13,25,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-530,Discontinued,Q1'10,2,4,32,N/A,2.93,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-540,Discontinued,Q1'10,2,4,32,N/A,3.06,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-520M,Discontinued,Q1'10,2,4,32,2.93,2.40,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-520UM,Discontinued,Q1'10,2,4,32,1.87,1.07,18,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-330M,Discontinued,Q1'10,2,4,32,N/A,2.13,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-640UM,Discontinued,Q1'10,2,4,32,2.27,1.20,18,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-980X Extreme Edition,Discontinued,Q1'10,6,12,32,3.60,3.33,130,12,Intel Smart Cache,N/A
Core i7-970,Discontinued,Q3'10,6,12,32,3.46,3.20,130,12,Intel Smart Cache,N/A
Core i7-620LE,Discontinued,Q1'10,2,4,32,2.80,2.00,25,4,Intel Smart Cache,Yes (Name Unknown)
Core i7-620UE,Discontinued,Q1'10,2,4,32,2.13,1.06,18,4,Intel Smart Cache,Yes (Name Unknown)
Core i5-520E,Discontinued,Q1'10,2,4,32,2.93,2.40,35,3,Intel Smart Cache,Yes (Name Unknown)
Core i7-610E,Discontinued,Q1'10,2,4,32,3.20,2.53,35,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-330E,Discontinued,Q1'10,2,4,32,N/A,2.13,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-760,Discontinued,Q3'10,4,4,45,3.33,2.80,95,8,Intel Smart Cache,N/A
Core i7-870S,Discontinued,Q2'10,4,8,45,3.60,2.66,82,8,Intel Smart Cache,N/A
Core i7-875K,Discontinued,Q2'10,4,8,45,3.60,2.93,95,8,Intel Smart Cache,N/A
Core i7-880,Discontinued,Q2'10,4,8,45,3.73,3.06,95,8,Intel Smart Cache,N/A
Core i5-680,Discontinued,Q2'10,2,4,32,3.86,3.60,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-550,Discontinued,Q2'10,2,4,32,N/A,3.20,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-655K,Discontinued,Q2'10,2,4,32,3.46,3.20,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-370M,Discontinued,Q3'10,2,4,32,N/A,2.40,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-330UM,Discontinued,Q2'10,2,4,32,N/A,1.20,18,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-450M,Discontinued,Q2'10,2,4,32,2.66,2.40,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-430UM,Discontinued,Q2'10,2,4,32,1.73,1.20,18,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-740QM,Discontinued,Q3'10,4,8,45,2.93,1.73,45,6,Intel Smart Cache,N/A
Core i7-660UM,Discontinued,Q2'10,2,4,32,2.40,1.33,18,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-540UM,Discontinued,Q2'10,2,4,32,2.00,1.20,18,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-580M,Discontinued,Q3'10,2,4,32,3.33,2.66,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-560M,Discontinued,Q3'10,2,4,32,3.20,2.66,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-660LM,Discontinued,Q3'10,2,4,32,3.06,2.26,25,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-680UM,Discontinued,Q3'10,2,4,32,2.53,1.46,18,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-560UM,Discontinued,Q3'10,2,4,32,2.13,1.33,18,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-640M,Discontinued,Q3'10,2,4,32,3.46,2.80,35,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-660UE,Discontinued,Q1'10,2,4,32,2.40,1.33,18,4,N/A,Intel HD Graphics for Previous Gen Intel Processors
Core i5-470UM,Discontinued,Q4'10,2,4,32,1.86,1.33,18,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-380UM,Discontinued,Q4'10,2,4,32,N/A,1.33,18,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i7-2720QM,Discontinued,Q1'11,4,8,32,3.30,2.20,45,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2540M,Discontinued,Q1'11,2,4,32,3.30,2.60,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-560,Discontinued,Q3'10,2,4,32,N/A,3.33,73,4,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-380M,Discontinued,Q3'10,2,4,32,N/A,2.53,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-460M,Discontinued,Q3'10,2,4,32,2.80,2.53,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i5-2300,Discontinued,Q1'11,4,4,32,3.10,2.80,95,6,Intel Smart Cache,Intel HD 2000 Graphics
Core i5-2400,Discontinued,Q1'11,4,4,32,3.40,3.10,95,6,Intel Smart Cache,Intel HD 2000 Graphics
Core i5-2400S,Discontinued,Q1'11,4,4,32,3.30,2.50,65,6,Intel Smart Cache,Intel HD 2000 Graphics
Core i5-2500,Discontinued,Q1'11,4,4,32,3.70,3.30,95,6,Intel Smart Cache,Intel HD 2000 Graphics
Core i5-2500K,Discontinued,Q1'11,4,4,32,3.70,3.30,95,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2500S,Discontinued,Q1'11,4,4,32,3.70,2.70,65,6,Intel Smart Cache,Intel HD 2000 Graphics
Core i5-2500T,Discontinued,Q1'11,4,4,32,3.30,2.30,45,6,Intel Smart Cache,Intel HD 2000 Graphics
Core i7-2600,Discontinued,Q1'11,4,8,32,3.80,3.40,95,8,Intel Smart Cache,Intel HD 2000 Graphics
Core i7-2600K,Discontinued,Q1'11,4,8,32,3.80,3.40,95,8,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2600S,Discontinued,Q1'11,4,8,32,3.80,2.80,65,8,Intel Smart Cache,Intel HD 2000 Graphics
Core i7-2630QM,Discontinued,Q1'11,4,8,32,2.90,2.00,45,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2310M,Discontinued,Q1'11,2,4,32,N/A,2.10,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2410M,Discontinued,Q1'11,2,4,32,2.90,2.30,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2820QM,Discontinued,Q1'11,4,8,32,3.40,2.30,45,8,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2520M,Discontinued,Q1'11,2,4,32,3.20,2.50,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2620M,Discontinued,Q1'11,2,4,32,3.40,2.70,35,4,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2920XM Extreme Edition,Discontinued,Q1'11,4,8,32,3.50,2.50,55,8,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-990X Extreme Edition,Discontinued,Q1'11,6,12,32,3.73,3.46,130,12,Intel Smart Cache,N/A
Core i5-480M,Discontinued,Q1'11,2,4,32,2.93,2.66,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-390M,Discontinued,Q1'11,2,4,32,N/A,2.66,35,3,Intel Smart Cache,Intel HD Graphics for Previous Gen Intel Processors
Core i3-2100,Discontinued,Q1'11,2,4,32,N/A,3.10,65,3,Intel Smart Cache,Intel HD 2000 Graphics
Core i3-2100T,Discontinued,Q1'11,2,4,32,N/A,2.50,35,3,Intel Smart Cache,Intel HD 2000 Graphics
Core i3-2102,Discontinued,Q2'11,2,4,32,N/A,3.10,65,3,Intel Smart Cache,Intel HD 2000 Graphics
Core i3-2120,Discontinued,Q1'11,2,4,32,N/A,3.30,65,3,Intel Smart Cache,Intel HD 2000 Graphics
Core i3-2120T,Discontinued,Q3'11,2,4,32,N/A,2.60,35,3,Intel Smart Cache,Intel HD 2000 Graphics
Core i3-2130,Discontinued,Q3'11,2,4,32,N/A,3.40,65,3,Intel Smart Cache,Intel HD 2000 Graphics
Core i3-2312M,Discontinued,Q2'11,2,4,32,N/A,2.10,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-2330E,Discontinued,Q2'11,2,4,32,N/A,2.20,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-2330M,Discontinued,Q2'11,2,4,32,N/A,2.20,35,3,L3 Cache,Intel HD 3000 Graphics
Core i3-2350M,Discontinued,Q4'11,2,4,32,N/A,2.30,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-2370M,Discontinued,Q1'12,2,4,32,N/A,2.40,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2310,Discontinued,Q2'11,4,4,32,3.20,2.90,95,6,Intel Smart Cache,Intel HD 2000 Graphics
Core i5-2320,Discontinued,Q3'11,4,4,32,3.30,3.00,95,6,Intel Smart Cache,Intel HD 2000 Graphics
Core i5-2390T,Discontinued,Q1'11,2,4,32,3.50,2.70,35,3,Intel Smart Cache,Intel HD 2000 Graphics
Core i5-2430M,Discontinued,Q4'11,2,4,32,3.00,2.40,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2450M,Discontinued,Q1'12,2,4,32,3.10,2.50,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2510E,Discontinued,Q1'11,2,4,32,3.10,2.50,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2635QM,Discontinued,Q1'11,4,8,32,2.90,2.00,45,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2640M,Discontinued,Q4'11,2,4,32,3.50,2.80,35,4,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2670QM,Discontinued,Q4'11,4,8,32,3.10,2.20,45,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2675QM,Discontinued,Q4'11,4,8,32,3.10,2.20,45,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2710QE,Discontinued,Q1'11,4,8,32,3.00,2.10,45,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2760QM,Discontinued,Q4'11,4,8,32,3.50,2.40,45,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2860QM,Discontinued,Q4'11,4,8,32,3.60,2.50,45,8,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2960XM Extreme Edition,Discontinued,Q4'11,4,8,32,3.70,2.70,55,8,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2629M,Discontinued,Q1'11,2,4,32,3.00,2.10,25,4,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2649M,Discontinued,Q1'11,2,4,32,3.20,2.30,25,4,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2657M,Discontinued,Q1'11,2,4,32,2.70,1.60,17,4,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2617M,Discontinued,Q1'11,2,4,32,2.60,1.50,17,4,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2677M,Discontinued,Q2'11,2,4,32,2.90,1.80,17,4,L3 Cache,Intel HD 3000 Graphics
Core i7-2637M,Discontinued,Q2'11,2,4,32,2.80,1.70,17,4,L3 Cache,Intel HD 3000 Graphics
Core i7-2537M,Discontinued,Q1'11,2,4,32,2.30,1.40,17,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2557M,Discontinued,Q2'11,2,4,32,2.70,1.70,17,3,L3 Cache,Intel HD 3000 Graphics
Core i7-2357M,Discontinued,Q2'11,2,4,32,N/A,1.30,17,3,L3 Cache,Intel HD 3000 Graphics
Core i7-2655LE,Discontinued,Q1'11,2,4,32,2.90,2.20,25,4,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-2310E,Discontinued,Q1'11,2,4,32,N/A,2.10,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2715QE,Discontinued,Q1'11,4,8,32,3.00,2.10,45,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2610UE,Discontinued,Q1'11,2,4,32,2.40,1.50,17,4,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-2340UE,Discontinued,Q2'11,2,4,32,N/A,1.30,17,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2515E,Discontinued,Q1'11,2,4,32,3.10,2.50,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-2377M,Discontinued,Q2'12,2,4,32,N/A,1.50,17,3,Intel Smart Cache,Yes (Name Unknown)
Core i5-2405S,Discontinued,Q2'11,4,4,32,3.30,2.50,65,6,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-2105,Discontinued,Q2'11,2,4,32,N/A,3.10,65,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2467M,Discontinued,Q2'11,2,4,32,2.30,1.60,17,3,L3 Cache,Intel HD 3000 Graphics
Core i7-980,Discontinued,Q2'11,6,12,32,3.60,3.33,130,12,Intel Smart Cache,N/A
Core i3-2125,Discontinued,Q3'11,2,4,32,N/A,3.30,65,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-2367M,Discontinued,Q4'11,2,4,32,N/A,1.40,17,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2435M,Discontinued,Q4'11,2,4,32,3.00,2.40,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i7-2700K,Discontinued,Q4'11,4,8,32,3.90,3.50,95,8,Intel Smart Cache,Intel HD 3000 Graphics
Core i5-2450P,Discontinued,Q1'12,4,4,32,3.50,3.20,95,6,Intel Smart Cache,Yes (Name Unknown)
Core i5-2380P,Discontinued,Q1'12,4,4,32,3.40,3.10,95,6,Intel Smart Cache,Yes (Name Unknown)
Core i7-3820QM,Discontinued,Q2'12,4,8,22,3.70,2.70,45,8,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3720QM,Discontinued,Q2'12,4,8,22,3.60,2.60,45,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3520M,Discontinued,Q2'12,2,4,22,3.60,2.90,35,4,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3360M,Discontinued,Q2'12,2,4,22,3.50,2.80,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3320M,Discontinued,Q2'12,2,4,22,3.30,2.60,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3667U,Discontinued,Q2'12,2,4,22,3.20,2.00,17,4,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3610QM,Discontinued,Q2'12,4,8,22,3.30,2.30,45,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3615QM,Discontinued,Q2'12,4,8,22,3.30,2.30,45,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3612QM,Discontinued,Q2'12,4,8,22,3.10,2.10,35,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3427U,Discontinued,Q2'12,2,4,22,2.80,1.80,17,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3330,Discontinued,Q3'12,4,4,22,3.20,3.00,77,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3330S,Discontinued,Q3'12,4,4,22,3.20,2.70,65,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3450,Discontinued,Q2'12,4,4,22,3.50,3.10,77,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3450S,Discontinued,Q2'12,4,4,22,3.50,2.80,65,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3475S,Discontinued,Q2'12,4,4,22,3.60,2.90,65,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3550,Discontinued,Q2'12,4,4,22,3.70,3.30,77,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3550S,Launched,Q2'12,4,4,22,3.70,3.00,65,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3570K,Discontinued,Q2'12,4,4,22,3.80,3.40,77,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3570T,Discontinued,Q2'12,4,4,22,3.30,2.30,45,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i7-3770K,Discontinued,Q2'12,4,8,22,3.90,3.50,77,8,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3770S,Discontinued,Q2'12,4,8,22,3.90,3.10,65,8,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3770T,Discontinued,Q2'12,4,8,22,3.70,2.50,45,8,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-2550K,Discontinued,Q1'12,4,4,32,3.80,3.40,95,6,Intel Smart Cache,Yes (Name Unknown)
Core i3-3240,Discontinued,Q3'12,2,4,22,N/A,3.40,55,3,Intel Smart Cache,Intel HD 2500 Graphics
Core i3-3225,Discontinued,Q3'12,2,4,22,N/A,3.30,55,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3220,Discontinued,Q3'12,2,4,22,N/A,3.30,55,3,Intel Smart Cache,Intel HD 2500 Graphics
Core i3-3220T,Discontinued,Q3'12,2,4,22,N/A,2.80,35,3,Intel Smart Cache,Intel HD 2500 Graphics
Core i3-3217UE,Launched,Q3'12,2,4,22,N/A,1.60,17,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3217U,Discontinued,Q2'12,2,4,22,N/A,1.80,17,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3120ME,Launched,Q3'12,2,4,22,N/A,2.40,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3110M,Discontinued,Q2'12,2,4,22,N/A,2.40,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3570S,Discontinued,Q2'12,4,4,22,3.80,3.10,65,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3570,Discontinued,Q2'12,4,4,22,3.80,3.40,77,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3470T,Discontinued,Q2'12,2,4,22,3.60,2.90,35,3,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3610ME,Launched,Q2'12,2,4,22,3.30,2.70,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3317U,Discontinued,Q2'12,2,4,22,2.60,1.70,17,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3210M,Discontinued,Q2'12,2,4,22,3.10,2.50,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3615QE,Launched,Q2'12,4,8,22,3.30,2.30,45,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3612QE,Launched,Q2'12,4,8,22,3.10,2.10,35,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3610QE,Launched,Q2'12,4,8,22,3.30,2.30,45,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3555LE,Launched,Q2'12,2,4,22,3.20,2.50,25,4,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3517UE,Launched,Q2'12,2,4,22,2.80,1.70,17,4,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3517U,Discontinued,Q2'12,2,4,22,3.00,1.90,17,4,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3770,Discontinued,Q2'12,4,8,22,3.90,3.40,77,8,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3240T,Discontinued,Q3'12,2,4,22,N/A,2.90,35,3,Intel Smart Cache,Intel HD 2500 Graphics
Core i3-3210M,Discontinued,Q2'12,2,4,22,3.10,2.50,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3612QM,Discontinued,Q2'12,4,8,22,3.10,2.10,35,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3470S,Discontinued,Q2'12,4,4,22,3.60,2.90,65,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3470,Discontinued,Q2'12,4,4,22,3.60,3.20,77,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i3-2115C,Launched,Q2'12,2,4,N/A,N/A,2.00,25,3,Intel Smart Cache,N/A
Core i5-3350P,Discontinued,Q3'12,4,4,22,3.30,3.10,69,6,Intel Smart Cache,N/A
Core i3-2365M,Discontinued,Q3'12,2,4,32,N/A,1.40,17,3,Intel Smart Cache,Yes (Name Unknown)
Core i7-3840QM,Discontinued,Q3'12,4,8,22,3.80,2.80,45,8,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3740QM,Discontinued,Q3'12,4,8,22,3.70,2.70,45,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-2328M,Discontinued,Q3'12,2,4,32,N/A,2.20,35,3,N/A,Intel HD 3000 Graphics
Core i3-3210,Discontinued,Q1'13,2,4,22,N/A,3.20,55,3,Intel Smart Cache,Intel HD 2500 Graphics
Core i7-3540M,Discontinued,Q1'13,2,4,22,3.70,3.00,35,4,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3380M,Discontinued,Q1'13,2,4,22,3.60,2.90,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3340M,Discontinued,Q1'13,2,4,22,3.40,2.70,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3687U,Discontinued,Q1'13,2,4,22,3.30,2.10,17,4,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3437U,Discontinued,Q1'13,2,4,22,2.90,1.90,17,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3632QM,Discontinued,Q3'12,4,8,22,3.20,2.20,35,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3630QM,Discontinued,Q3'12,4,8,22,3.40,2.40,45,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3635QM,Discontinued,Q3'12,4,8,22,3.40,2.40,45,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3120M,Discontinued,Q3'12,2,4,22,N/A,2.50,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i7-3632QM,Discontinued,Q3'12,4,8,22,3.20,2.20,35,6,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3229U,Discontinued,Q1'13,2,4,22,N/A,1.40,13,3,N/A,Intel HD 4000 Graphics
Core i5-3339Y,Discontinued,Q1'13,2,4,22,2.00,1.50,13,3,N/A,Intel HD 4000 Graphics
Core i5-3439Y,Discontinued,Q1'13,2,4,22,2.30,1.50,13,3,N/A,Intel HD 4000 Graphics
Core i7-3689Y,Discontinued,Q1'13,2,4,22,2.60,1.50,13,4,N/A,Intel HD 4000 Graphics
Core i7-3537U,Discontinued,Q1'13,2,4,22,3.10,2.00,17,4,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3337U,Discontinued,Q1'13,2,4,22,2.70,1.80,17,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3230M,Discontinued,Q1'13,2,4,22,3.20,2.60,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3227U,Discontinued,Q1'13,2,4,22,N/A,1.90,17,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-3130M,Discontinued,Q1'13,2,4,22,N/A,2.60,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3230M,Discontinued,Q1'13,2,4,22,3.20,2.60,35,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i3-2375M,Discontinued,Q1'13,2,4,32,N/A,1.50,17,3,Intel Smart Cache,Yes (Name Unknown)
Core i3-2348M,Discontinued,Q1'13,2,4,32,N/A,2.30,35,3,Intel Smart Cache,Intel HD 3000 Graphics
Core i3-3250,Discontinued,Q2'13,2,4,22,N/A,3.50,55,3,Intel Smart Cache,Intel HD 2500 Graphics
Core i3-3250T,Discontinued,Q2'13,2,4,22,N/A,3.00,35,3,Intel Smart Cache,Intel HD 2500 Graphics
Core i3-3245,Discontinued,Q2'13,2,4,22,N/A,3.40,55,3,Intel Smart Cache,Intel HD 4000 Graphics
Core i5-3340,Discontinued,Q3'13,4,4,22,3.30,3.10,77,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i5-3340S,Discontinued,Q3'13,4,4,22,3.30,2.80,65,6,Intel Smart Cache,Intel HD 2500 Graphics
Core i3-3115C,Launched,Q3'13,2,4,22,N/A,2.50,25,4,L3 Cache,N/A
"""

data = []
for x in raw_data.strip().split("\n"):
    name = x.split(",")[0]
    if len(name.split()) != 2:
        continue
    if name.split()[0] == "Core2":
        continue
    if name[-1].lower() in 'abcdefghijklmnopqrstuvwxyz':
        continue
    if name.split()[-1].lower()[0] != 'i':
        continue
    data.append(x)

for x in data:
    break
    print('\t'.join(str(x).split(',')))

string = """
1666418547
1666567215
1665002006
1664832077
1665185061
1665377576
1666464292
1665714559
1665929486
1667151249"""

final = []

for x in string.strip().split("\n"):
    final.append(int(x))


final.sort()

print('\n'.join([str(x) for x in final]))
