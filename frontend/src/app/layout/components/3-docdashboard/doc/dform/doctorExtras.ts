import { FormGroup, FormArray, FormControl } from "@angular/forms";

export const SPECIALIZATION_CHOICES: [string, string][] = [
    
    ["general_practice", "General Practice"],
    ["child_care", "Child Care"],
    ["women_health", "Women Health"],
    ["bone_joint_care", "Bone & Joint Care"],
    ["heart_care", "Heart Care"],
    ["skin_care", "Skin Care"],
    ["eye_care", "Eye Care"],
    ["dental_care", "Dental Care"],
    ["mental_health", "Mental Health"],
    ["brain_nervous_system_care", "Brain & Nervous System Care"],
    ["digestive_health", "Digestive Health"],
    ["urinary_tract_health", "Urinary Tract Health"],
    ["cancer_care", "Cancer Care"],
    ["ear_nose_throat_care", "Ear, Nose & Throat Care"],
    ["hormone_health", "Hormone Health"],
    ["joint_health", "Joint Health"],
    ["allergy_immune_system_care", "Allergy & Immune System Care"],
    ["lung_respiratory_health", "Lung & Respiratory Health"],
    ["kidney_health", "Kidney Health"],
    ["physical_therapy", "Physical Therapy"]  
];

export const QUALIFICATION_CHOICES: [string, string][] = [

    ["mbbs", "MBBS"],
    ["bds", "BDS"],
    ["md", "MD"]


];

export const availableDays: string[] = [
  'monday',
  'tuesday',
  'wednesday',
  'thursday',
  'friday',
  'saturday',
  'sunday'
];




// function to store avaiaiableb weekends of doctor 


export function onChange(e: any, form: FormGroup) {
  const checkedvalue = e.target.value;
  const checkedflag = e.target.checked;

  const checkedArray = form.get('availability_data.days') as FormArray;
  if (checkedflag) {
    checkedArray.push(new FormControl(checkedvalue))
  } else {
    let i: number = 0;
    checkedArray.controls.forEach((item) => {
      if (item.value == checkedflag) {
        checkedArray.removeAt(i);
      }
      i++;
    })
  }
}
