import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SearchbarRoutingModule } from './searchbar-routing.module';
import { SearchbarComponent } from './searchbar.component';



import { FormsModule } from '@angular/forms';

import {MatIconModule} from '@angular/material/icon';
import {MatSelectModule} from '@angular/material/select';

@NgModule({
  declarations: [
    SearchbarComponent
  ],
  imports: [
    CommonModule,
    SearchbarRoutingModule,
    MatIconModule,
    MatSelectModule,
    FormsModule
  ]
})
export class SearchbarModule { }
