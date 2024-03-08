import { Component } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { PatientService } from '../services/patient/patient.service';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  form!: FormGroup;

  constructor(private formBuilder: FormBuilder,private patientService:PatientService) {}
  
  ngOnInit(): void {
  
  this.form = this.formBuilder.group( {
  
    age:'',

    sex:'',

    blood_group:'',

    weight:'',

    height:'',

    bmi:''
  
  
  });
  
  }
  submit() {
    this.patientService.register(this.form.getRawValue()).subscribe(
      (res)=>console.log(res)
    )
  }
}
