import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';

const materialcomponents=[
  MatToolbarModule,MatButtonModule
]


@NgModule({
  
  imports: [CommonModule,materialcomponents],
  exports:[materialcomponents]
})
export class MaterialModule { }
