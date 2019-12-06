package ej1;

class App {
	
	public static void main(String args[]) {
		
		try {
			
			//Instancia una Matriz que exede las columnas.
			MatrizObjetos matriz = new MatrizObjetos(500, 100);
			
			
			String st1 = new String(" esto es un String ");
			Integer entero = new Integer(10);
			
			matriz.SetRowCol(0, 0, st1);
			matriz.SetRowCol(1, 0, entero);
			
			System.out.println(matriz.GetRowCol(0, 0));
			matriz.SetRowCol(10, 0, st1);
			
			System.out.println(matriz);

		} catch (MatrizException e) {
			
			System.out.println(e.toString());
		}
	}
}
