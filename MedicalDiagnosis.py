#!/usr/bin/env python
# coding: utf-8

# In[4]:


Symptoms = ["None", "Fever", "Pain in Abdomen especially ILIAC FOSSA", "vomiting", "Cough",
            "Pain in chest","Nausea","Feeling weak","Jaundice","Digestion Disorder",
            "Dark Urine","Pain in right side of Abdomen","Fatigue","Loss of appetite",
            "Bleeding easily","Bruising Easily","Itchy Skin","Joint Pain","Blood in the urine",
            "Hoarseness","Persistent lumps or swollen glands", "Obvious change in a wart or a mole",
            "Indigestion or difficulty swallowing","Unexpected weight loss/night sweats or fever",
            "Difficulty In Breathing/Shortness of Breath","Chest pain or pressure","loss of speech or movement",
            "Loss of taste or smell","Sore throat",
            "Headaches, which may be severe and worsen with activity or in the early morning","Seizures",
            "Personality or memory changes","Drowsiness","Sleep problems","Memory problems" ]

Test = ["None", "Blood CP with ESR... TLC (Total leucocyte count) will be high", 
        "DLC (Differential leucocyte count) Neutrophils will be high", "ESR high",
        "X-ray chest: pneumonic patch (sometimes)", "Examine throat: (Red enlarged tonsils, pus in tonsils)",
        "Blood Samples with more than one kind of hepatitis virus",
        "Abnormal blood cells"]
Treatment = ["None", "Surgery", "Antibiotics", 
             "anti-allergic, paracetamol. If not gone, Add antibiotics orally. If not gone and Add antibiotics IV",
             "AntiViral Medications\n","Chemotherapy\n",
             "you should rest, drink plenty of fluid, and eat nutritious food. Stay in a separate room from other family members\n",
             "surgery\n"]
Disease = ["None", "Acute appendicitis", "Pneumonia", "Acute Tonsilitis", "Hepatitis","Cancer",
           "Covid-19" ,"Brain Tumor","\n\n**Unable To Diagnose**",]

print("\t\t\t\t Welcome to Medical Diagnosis System\n ****************************************************************************************************************************** \n In order to diagnose your disease you have to Enter the symptoms and test reports into the system \n Given below are different symptoms. You have to select any of the options as per your symptoms. \n")
def PrintSymptoms():
    print(" 1. Fever\n", 
          "2. Pain in Abdomen especially ILIAC FOSSA\n", 
          "3. vomiting\n", "4. Cough\n",
          "5. Pain in chest\n","6. Nausea\n",
          "7. Feeling weak\n","8. Jaundice\n","9. Digestion Disorder\n",
          "10. Dark Urine\n","11. Pain in right side of Abdomen\n","12. Fatigue\n",
          "13. Loss of appetite\n","14. Bleeding easily\n","15. Bruising Easily\n",
          "16. Itchy Skin\n","17. Joint Pain\n","18. Blood in the urine\n","19. Hoarseness\n",
          "20. Persistent lumps or swollen glands\n", "21. Obvious change in a wart or a mole\n",
          "22. Indigestion or difficulty swallowing\n","23. Unexpected weight loss/night sweats or fever\n",
         "24. Difficulty In Breathing/Shortness of Breath\n","25. Chest pain or pressure\n",
          "26. loss of speech or movement\n","27. Loss of taste or smell\n","28. Sore throat\n",
         "29. Headaches, which may be severe and worsen with activity or in the early morning\n","30. Seizures\n",
            "31. Personality or memory changes\n","32. Drowsiness\n","33. Sleep problems\n","34. Memory problems\n")

def PrintTests():
    print(" 1. Blood CP with ESR... TLC (Total leucocyte count) will be high\n", "2. DLC (Differential leucocyte count) Neutrophils will be high\n", "3. ESR high\n", "4. X-ray chest: pneumonic patch (sometimes)\n", "5. Examine throat: (Red enlarged tonsils, pus in tonsils)\n","6. Blood Samples with more than one kind of hepatitis virus","7. Blood Test: Abnormal blood cells")



def DetectDisease(ListSymptoms, ListTest):
    #Start Diagnose
    DiseaseDetect = 0
    #Start Acute appendicitis
    if len(ListSymptoms) == 3 and len(ListTest) == 3:
        if ListSymptoms[0] == 1 and ListSymptoms[1] == 2 and ListSymptoms[2] == 3:
            if ListTest[0] == 1 and ListTest[1] == 2 and ListTest[2] == 3:
                DiseaseDetect = 1
                return 1
            else:
                DiseaseDetect = 8
        else:
            DiseaseDetect = 8
    else:
        DiseaseDetect = 8
    #End Acute appendicitis
    #start Hepatitis
    if len(ListSymptoms) >= 4 or len(ListSymptoms) <= 8 and len(ListTest) == 1:
        if ListSymptoms[0] == 1 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 and ListSymptoms[1] == 1 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 and ListSymptoms[2] == 1 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 and ListSymptoms[3] == 1 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 and ListSymptoms[4] == 1 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 and ListSymptoms[5] == 1 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 and ListSymptoms[6] == 1 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 and ListSymptoms[7] == 1 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17:
            if ListTest[0] == 6:
                DiseaseDetect = 4
                return 4
            else:
                DiseaseDetect = 8
        else:
            DiseaseDetect = 8
    else:
        DiseaseDetect =8
    #End Hepatitis
    
    
    
    
    #Start Cancer
    if len(ListSymptoms) >= 3 or len(ListSymptoms)<=6 and len(ListTest) == 1:
        if ListSymptoms[0] == 18 or 19 or 20 or 21 or 22 or 23 and ListSymptoms[1] == 18 or 19 or 20 or 21 or 22 or 23 and ListSymptoms[2] == 18 or 19 or 20 or 21 or 22 or 23 and ListSymptoms[3] == 18 or 19 or 20 or 21 or 22 or 23 and ListSymptoms[4] == 18 or 19 or 20 or 21 or 22 or 23 and ListSymptoms[5] == 18 or 19 or 20 or 21 or 22 or 23:
            if ListTest[0] == 8:
                DiseaseDetect = 5
                return 5
            else:
                DiseaseDetect = 8
        else:
            DiseaseDetect = 8
    else:
        DiseaseDetect = 8
    #End Cancer
     
    #Start Covid
    if len(ListSymptoms) >= 3 or len(ListSymptoms) <=5 and len(ListTest) == 1:
        if ListSymptoms[0] == 24 or 25 or 26 or 27 or 28 and ListSymptoms[1] == 24 or 25 or 26 or 27 or 28 and ListSymptoms[2] == 24 or 25 or 26 or 27 or 28 and ListSymptoms[3] == 24 or 25 or 26 or 27 or 28 and ListSymptoms[4] == 24 or 25 or 26 or 27 or 28:
            if ListTest[0] == 0:
                DiseaseDetect = 6
                return 6
            else:
                DiseaseDetect = 8
        else:
            DiseaseDetect = 8
    else:
        DiseaseDetect = 8
    #End Covid
    #Start Brain T
    if len(ListSymptoms) >= 3 or len(ListSymptoms)<=6 and len(ListTest) == 1:
        if ListSymptoms[0] == 29 or 30 or 31 or 32 or 33 or 34 and ListSymptoms[1] == 29 or 30 or 31 or 32 or 33 or 34 and ListSymptoms[2] == 29 or 30 or 31 or 32 or 33 or 34 and ListSymptoms[3] == 29 or 30 or 31 or 32 or 33 or 34 and ListSymptoms[4] == 29 or 30 or 31 or 32 or 33 or 34 and ListSymptoms[5] == 29 or 30 or 31 or 32 or 33 or 34:
            if ListTest[0] == 0:
                DiseaseDetect = 7
                return 7
            else:
                DiseaseDetect = 8
        else:
            DiseaseDetect = 8
    else:
        DiseaseDetect = 8
    #End Brain T
    
    
    #Start Pneumonia
    if len(ListSymptoms) == 3 and len(ListTest) == 4:
        if ListSymptoms[0] == 1 and ListSymptoms[1] == 4 and ListSymptoms[2] == 5:
            if ListTest[0] == 1 and ListTest[1] == 2 and ListTest[2] == 3 and ListTest[3] == 4:
                DiseaseDetect = 2
                return 2
            else:
                DiseaseDetect = 8
        else:
            DiseaseDetect = 8
    else:
        DiseaseDetect = 8
    #End Pneumonia

    #Start Acute Tonsilitis:
    if len(ListSymptoms) == 2 and len(ListTest) == 1:
        if ListSymptoms[0] == 1 and ListSymptoms[1] == 4:
            if ListTest[0] == 5:
                DiseaseDetect = 3
                return 3
            else:
                DiseaseDetect = 8
        else:
            DiseaseDetect = 8
    else:
        DiseaseDetect = 8
    #End Acute Tonsilitis

    return DiseaseDetect
    #End Diagnose

#End Function



#Start Input Symptoms
PrintSymptoms()
print ("Select Symptoms You Have")
More = 'y'
i = 0
ListSymptoms = []
while More == 'y':
    i = i + 1
    print(i, end='')
    x = int(input( ". "))
    More = input("More (y/n) = ")
    ListSymptoms.append(x)
#End Input Symptoms

#Start Sort
ListSymptoms.sort()
#End Sort

#Start Input Tests
PrintTests()
print ("Select Test You Have Done")
More = 'y'
i = 0
ListTest = []
while More == 'y':
    i = i + 1
    print(i, end='')
    x = int(input( ". "))
    More = input("More (y/n) = ")
    ListTest.append(x)
#End Input Tests

#Start Sort
ListTest.sort()
#End Sort


Index = DetectDisease(ListSymptoms, ListTest)
if Index == 5:
    print(Disease[Index])
else:
    if Disease[Index]=='Acute appendicitis':
        Treatment[Index]='Surgery'
    if Disease[Index]=='Pneumonia':
        Treatment[Index]='Antibiotics'
    if Disease[Index]=='Acute Tonsilitis':
        Treatment[Index]='anti-allergic, paracetamol. If not gone, add antibiotics orally. If not gone, add antibiotics IV'
    if Disease[Index]=='Hepatitis':
        Treatment[Index]='AntiViral Medications'
    if Disease[Index]=='Cancer':
        Treatment[Index]='Chemotherapy'
    if Disease[Index]=='Covid-19':
        Treatment[Index]='you should rest, drink plenty of fluid, and eat nutritious food. Stay in a separate room from other family members'
    if Disease[Index]=='Brain Tumor':
        Treatment[Index]='surgery'
    print("\n\nSORRY!, But you may be suffering from Disease: ", Disease[Index])
    print("Recommended Treatment : ", Treatment[Index])


# In[ ]:





# In[ ]:





# In[ ]:




