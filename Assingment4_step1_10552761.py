Ri={"name":"Ri","type":"conv","area":0.25,"hconv":10}
Ro={"name":"Ro","type":"conv","area":0.25,"hconv":25}
R1={"name":"R1","type":"cond","area":0.25,"length":0.03,"k":0.026}
R2={"name":"R2","type":"cond","area":0.25,"length":0.02,"k":0.22}
R3={"name":"R3","type":"cond","area":0.015,"length":0.16,"k":0.22}
R4={"name":"R4","type":"cond","area":0.22,"length":0.16,"k":0.72}
R5={"name":"R5","type":"cond","area":0.015,"length":0.16,"k":0.22}
R6={"name":"R6","type":"cond","area":0.25,"length":0.02,"k":0.22}


resistances_in_series=[Ri,Ro,R1,R2,R6]
resistances_series_dictionary={"mode":"Series","name":"resistanceInSeries","ResistanceList":resistances_in_series}
resistances_in_parallel=[R3,R4,R5]
resistances_parallel_dictionary={"mode":"Parallel","name":"resistanceInParallel","ResistanceList":resistances_in_parallel}

#resistances_in_parallel_2=[R5,R6]
#resistances_parallel_2_dictionary={"mode":"Parallel","name":"resistanceInParallel2","ResistanceList":resistances_in_parallel_2}

wall_input_information=[resistances_series_dictionary,resistances_parallel_dictionary] #resistances_parallel_2_dictionary

#Rtotalwall=0
Rtotal_parallel_inv=0
Rtotalseries=0 

for anyresistance in wall_input_information:
 
    resistance_mode=anyresistance["mode"]
    
    resistanceinfo=anyresistance["ResistanceList"]
    
    if resistance_mode=="Series":
        
        for resistances in resistanceinfo:
            
            type_of_resistance=resistances["type"]
            
            if type_of_resistance=="cond":
                
                A=resistances["area"]
                L=resistances["length"]
                k=resistances["k"]
                R=round(float(L/(k*A)),2)
                
            elif type_of_resistance=="conv":
                A=resistances["area"]
                h=resistances["hconv"]
                R=round(float(1/(A*h)),2)
            
            resistances["ResistanceEachLayer"]=R 
            
            Rtotalseries=Rtotalseries+R
                
    elif resistance_mode=="Parallel":
        
        for resistances in resistanceinfo:
            
            type_of_resistance=resistances["type"]
            
            if type_of_resistance=="cond":
                
                A=resistances["area"]
                L=resistances["length"]
                k=resistances["k"]
                R=round(float(L/(k*A)),2)
                
            
            Rtotal_parallel_inv=Rtotal_parallel_inv+(1.0/R)
            Rparalell=(1.0/Rtotal_parallel_inv)
            
            resistances["ResistanceEachLayer"]=R 
      
            Rtotalwall=round(Rparalell+Rtotalseries,2)
      
   
Result={"Result_Ri":Ri["ResistanceEachLayer"],"Result_Ro":Ro["ResistanceEachLayer"],"Result_R1":R1["ResistanceEachLayer"],
"Result_R2":R2["ResistanceEachLayer"],"Result_R3":R3["ResistanceEachLayer"],"Result_R4":R4["ResistanceEachLayer"],
"Result_R5":R5["ResistanceEachLayer"],"Result_R6":R6["ResistanceEachLayer"]
}
    
wall_calculation_output={"InfoEachLayer in W/C":Result,"TotalWall_Value in W/C":Rtotalwall}

print wall_calculation_output
                        




   