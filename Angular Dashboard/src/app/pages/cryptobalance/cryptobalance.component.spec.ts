import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CryptobalanceComponent } from './cryptobalance.component';

describe('CryptobalanceComponent', () => {
  let component: CryptobalanceComponent;
  let fixture: ComponentFixture<CryptobalanceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CryptobalanceComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CryptobalanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
