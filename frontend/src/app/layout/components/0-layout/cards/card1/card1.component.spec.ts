import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Card1Component } from './card1.component';

describe('Card1Component', () => {
  let component: Card1Component;
  let fixture: ComponentFixture<Card1Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Card1Component]
    });
    fixture = TestBed.createComponent(Card1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
