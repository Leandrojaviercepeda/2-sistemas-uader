package ej1;

import java.util.*;

class MatrizObjetos {
	static int max_rows = 200;
	static int max_cols = 200;
	Vector cuerpo[];

	MatrizObjetos(int columnas, int filas) throws MatrizException {
		if (columnas > max_cols) {
			throw new MatrizException(Configuracion.getInstance().getMensaje("E1"));
		} else if (filas > max_rows) {
			throw new MatrizException(Configuracion.getInstance().getMensaje("E2"));
		} else {
			cuerpo = new Vector[filas];
			for (int i = 0; i < filas; i++)
				cuerpo[i] = new Vector(2);
		}
	}

	public void SetRowCol (int row, int col, Object obj) throws MatrizException{
		try {
			cuerpo[row].add(col, obj);
		} catch (Exception e) {
			if (col > max_cols || col < 0)
				throw new MatrizException(Configuracion.getInstance().getMensaje("E1"));
			else if(row > max_rows || row < 0)
				throw new MatrizException(Configuracion.getInstance().getMensaje("E2"));
		}
	}

	@SuppressWarnings("finally")
	public Object GetRowCol(int row, int col) throws MatrizException{
		Object obj = new Object();
		try {
			obj = cuerpo[row].elementAt(col);
		} catch (Exception e) {
			if (col > max_cols)
				throw new MatrizException(Configuracion.getInstance().getMensaje("E1"));
			else if(row > max_rows || row < 0)
				throw new MatrizException(Configuracion.getInstance().getMensaje("E2"));
			else if(col < 0)
				throw new MatrizException(Configuracion.getInstance().getMensaje("E3"));
			else if(row < 0)
				throw new MatrizException(Configuracion.getInstance().getMensaje("E4"));
		} finally {
			return obj;
		}
	}

	public String toString() {
		String staux = new String("");
		for (int i = 0; i < cuerpo.length; i++)
			for (int j = 0; j < cuerpo[i].size(); j++) {
				staux = staux + cuerpo[i].elementAt(j);
			}
		return staux;
	}
}