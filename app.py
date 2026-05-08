from flask import Flask, request, render_template, redirect, url_for
from config import conectar, desconectar
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/ProyectoSENA")
def index():
    return render_template("index.html")


# -------------------- REGISTRAR --------------------
@app.route("/ProyectoSENA/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        identificacion = request.form["identificacion"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        telefono = request.form["telefono"]
        cargo = request.form["cargo"]
        salario = request.form["salario"]
        departamento = request.form["departamento"]
        conexion = None
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO empleados
                (identificacion, nombre, apellido, telefono, cargo, salario, departamento)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (identificacion, nombre, apellido,
                                       telefono, cargo, salario, departamento))
            conexion.commit()
            cursor.close()
            print("Empleado registrado exitosamente")
            return redirect(url_for("consultar"))
        except sqlite3.Error as error:
            print("Error al registrar el empleado:", error)
            return f"Error al registrar el empleado: {error}"
        finally:
            if conexion:
                desconectar(conexion)
    return render_template("registrar.html")


# -------------------- CONSULTAR --------------------
@app.route("/ProyectoSENA/consultar")
def consultar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, identificacion, nombre, apellido, telefono, cargo, salario FROM empleados ORDER BY id")
    empleados = cursor.fetchall()
    cursor.close()
    desconectar(conexion)
    return render_template("consultar.html", empleados=empleados)


# -------------------- ELIMINAR --------------------
@app.route("/ProyectoSENA/eliminar", methods=["GET", "POST"])
def eliminar():
    mensaje = None
    if request.method == "POST":
        emp_id = request.form["id"]
        conexion = None
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM empleados WHERE id = ?", (emp_id,))
            conexion.commit()
            mensaje = (f"Empleado con id {emp_id} eliminado."
                       if cursor.rowcount else
                       f"No existe un empleado con id {emp_id}.")
            cursor.close()
        except sqlite3.Error as error:
            mensaje = f"Error al eliminar: {error}"
        finally:
            if conexion:
                desconectar(conexion)

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, identificacion, nombre, apellido FROM empleados ORDER BY id")
    empleados = cursor.fetchall()
    cursor.close()
    desconectar(conexion)
    return render_template("eliminar.html", empleados=empleados, mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
