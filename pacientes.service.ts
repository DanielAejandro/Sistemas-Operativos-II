import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Paciente {
  id?: number;
  nombre: string;
  enfermedad: string;
}

@Injectable({
  providedIn: 'root'
})
export class PacienteSService {
  private apiUrl = 'http://localhost:8000/pacientes';

  constructor(private http: HttpClient) {}

  obtenerPacienteS(): Observable<Paciente[]> {
    return this.http.get<Paciente[]>(this.apiUrl);
  }

  crearPaciente(paciente: Paciente): Observable<Paciente> {
    return this.http.post<Paciente>(this.apiUrl, paciente);
  }
}

