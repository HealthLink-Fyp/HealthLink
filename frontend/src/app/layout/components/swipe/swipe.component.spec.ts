import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SwipeComponent } from './swipe.component';

describe('SwipeComponent', () => {
  let component: SwipeComponent;
  let fixture: ComponentFixture<SwipeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SwipeComponent]
    });
    fixture = TestBed.createComponent(SwipeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
