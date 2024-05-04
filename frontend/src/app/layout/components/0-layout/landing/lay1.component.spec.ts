import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Lay1Component } from './lay1.component';

describe('Lay1Component', () => {
  let component: Lay1Component;
  let fixture: ComponentFixture<Lay1Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Lay1Component]
    });
    fixture = TestBed.createComponent(Lay1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
