import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SearchbarRoutingModule } from './searchbar-routing.module';
import { SearchbarComponent } from './searchbar.component';



import { FormsModule } from '@angular/forms';

import {MatIconModule} from '@angular/material/icon';
import {MatSelectModule} from '@angular/material/select';
import { MaterialModule } from 'src/app/material/material/material.module';

@NgModule({
  declarations: [
    SearchbarComponent
  ],
  imports: [
    CommonModule,
    SearchbarRoutingModule,
    MaterialModule
  ],
  exports:[SearchbarComponent]
})
export class SearchbarModule { }
