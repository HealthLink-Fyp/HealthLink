import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import {FormControl, Validators, FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import { MatFormFieldModule} from '@angular/material/form-field';

 const materialcomponents=[
  MatToolbarModule,MatButtonModule,
  MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule
   
]


@NgModule({
  
  imports: [materialcomponents],
  exports:[materialcomponents]
})
export class MaterialModule { }
