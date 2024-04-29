import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LayoutRoutingModule } from './layout-routing.module';
import { LayoutComponent } from './layout.component';

import {MatCardModule} from '@angular/material/card';
import { MaterialModule } from 'src/app/architecture/material/material/material.module';
import { Lay1Component } from './landing/lay1.component';
import { FooterComponent } from './footer/footer.component';

import { RouterModule } from '@angular/router';
import { LandingComponent } from '../topnav/landing.component';
import { LandingModule } from '../topnav/landing.module';
import { SearchbarModule } from '../searchbar/searchbar.module';

import { CardsComponent } from './cards/cards.component';
import { Card1Component } from './cards/card1/card1.component';
import { SwipeComponent } from './swipe/swipe.component';

@NgModule({
  declarations: [
    LayoutComponent,
    Lay1Component,
    CardsComponent,
    Card1Component,
    FooterComponent,
    SwipeComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
    LayoutRoutingModule,
    MaterialModule,
    LandingModule,
    SearchbarModule,
    
  ]
})
export class LayoutModule { }
