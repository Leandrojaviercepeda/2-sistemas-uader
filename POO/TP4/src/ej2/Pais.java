package ej2;

import java.util.ArrayList;

public class Pais {
	
	private String nombre;
	private Continente continentePropio;
	private ArrayList<Provincia> provincias;
	private ArrayList<Pais> paisesLimite;
	
	public Pais(String nombre, Continente continentePropio) {
		this.nombre = nombre;
		this.continentePropio = continentePropio;
		this.provincias = new ArrayList <Provincia>();
		this.paisesLimite = new ArrayList<Pais>();
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Continente getContinentePropio() {
		return continentePropio;
	}

	public void setContinentePropio(Continente continentePropio) {
		this.continentePropio = continentePropio;
	}

	public ArrayList<Pais> getPaisesLimite() {
		return paisesLimite;
	}

	public void setPaisesLimite(ArrayList<Pais> paisesLimite) {
		this.paisesLimite = paisesLimite;
	}

	public void agregarPaisLimite(Pais pais){
		paisesLimite.add(pais);
	}
	
	public ArrayList<Provincia> getProvincias() {
		return provincias;
	}

	public void setProvincias(ArrayList<Provincia> provincias) {
		this.provincias = provincias;
	}
	
	public void agregarProvincias(Provincia provincia){
		this.provincias.add(provincia);
	}

	public String mostrarProvincias(){
		String stringSalida = "";
		for (Provincia provincia : this.provincias) {
			stringSalida += provincia.getNombre() + ", ";
		}
		return stringSalida;
	}

	public String mostrarPaisesLimite(){
		String stringSalida = "";
		for (Pais pais : this.paisesLimite) {
			stringSalida += pais.getNombre() + ", ";
		}
		return stringSalida;
	}
	
}
