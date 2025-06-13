import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Receta {
  id?: number;
  nombre: string;
  especialidad: string;
}

@Injectable({
  providedIn: 'root'
})
export class RecetasService {
  private apiUrl = 'http://localhost:8000/recetaS';

  constructor(private http: HttpClient) {}

  obtenerRecetas(): Observable<Receta[]> {
    return this.http.get<Receta[]>(this.apiUrl);
  }

  crearReceta(receta: Receta): Observable<Receta> {
    return this.http.post<Receta>(this.apiUrl, receta);
  }
}

