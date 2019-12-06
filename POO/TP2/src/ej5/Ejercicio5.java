package ej5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ejercicio5 {

	/*
	 * Leer el nombre y sueldo de 5 empleados y mostrar el nombre y sueldo del
	 * empleado que más gana y el sueldo promedio.
	 */

	public static void main(String[] args) throws NumberFormatException, IOException {
		try {
			BufferedReader t = new BufferedReader(new InputStreamReader(System.in));
			System.out.println("Ingrese la cantidad de empleados");
			int qe = Integer.parseInt(t.readLine());
			int[] ls = listSalary(qe);
			String[] ln = listName(qe);
			dataEmployee(ln,ls);	
			int[] he = higherEmployee(ls);
			double ae = averageEmployee(ls);
			java.text.DecimalFormat formato = new java.text.DecimalFormat("0.00");
			System.out.println("El empleado con mayor salario es: " + ln[he[1]]);
			System.out.println("Su sueldo es: " + he[0]);
			System.out.println("El sueldo promedio es: " + formato.format(ae));	
		} catch (Exception e) {
			System.out.println("Error ingrese solo numeros");
		}
	}
	
	public static int[] listSalary(int quantEmployee){
		int[] ls = new int[quantEmployee];
		for (int i = 0; i < quantEmployee; i++){
			ls[i] = 0;
		}
		return ls;
	}
	
	public static String[] listName(int quantEmployee){
		String[] ln = new String[quantEmployee];
		for (int i = 0; i < quantEmployee; i++){
			ln[i] = "";
		}
		return ln;
	}
	
	public static void dataEmployee(String[] listName,int[] listSalary) throws IOException{		
		for (int i = 0; i < listSalary.length; i++) {
			BufferedReader t = new BufferedReader(new InputStreamReader(System.in));
			System.out.println("Ingrese el nombre del Empleado: ");
			String name = t.readLine();
			listName[i] = name;
			System.out.println("Ingrese el sueldo del Empleado: ");
			int salary = Integer.parseInt(t.readLine());
			listSalary[i] = salary;
		}
	}

	public static int[] higherEmployee(int[] listSalary) throws NumberFormatException, IOException{
		int[] higEmployee = {0,0};
		for (int i = 0; i < listSalary.length; i++){
			if (higEmployee[0] < listSalary[i]){
				higEmployee[0] = listSalary[i];
				higEmployee[1] = i;
			}
		}
		return higEmployee;
	}
	
	public static double averageEmployee(int[] listSalary){
		double average = 0;
		for (int i = 0; i < listSalary.length; i++){
			average += listSalary[i];
		}
		average /= listSalary.length;
		return average;
	}
	
}
