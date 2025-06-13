import { Component, OnInit } from '@angular/core';
import { DoctoresService, Doctor } from 'src/app/services/doctores.service';

@Component({
  selector: 'app-lista-doctores',
  templateUrl: './lista-doctores.component.html',
})
export class ListaDoctoresComponent implements OnInit {
  doctores: Doctor[] = [];

  constructor(private doctoresService: DoctoresService) {}

  ngOnInit(): void {
    this.doctoresService.obtenerDoctores().subscribe((data) => {
      this.doctores = data;
    });
  }
}

