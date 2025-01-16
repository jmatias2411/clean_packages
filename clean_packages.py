import pkg_resources
import subprocess

# Lista de paquetes que deseas conservar
keep_packages = [
    "numpy", "pandas", "matplotlib", "seaborn", "scipy", "scikit-learn",
    "statsmodels", "fastapi", "dask", "jupyter", "torch", "torchvision",
    "seaborn", "pip", "psutil", "requests", "schedule", "conda", "anaconda",
    "virtualenv", "ipykernels"
]

# Obtén la lista de todos los paquetes instalados
installed_packages = [pkg.project_name for pkg in pkg_resources.working_set]

# Filtra los paquetes que no están en la lista de conservación
packages_to_remove = [pkg for pkg in installed_packages if pkg.lower() not in keep_packages]

# Imprime la lista de paquetes a desinstalar
print("Paquetes a desinstalar:")
for pkg in packages_to_remove:
    print(f" - {pkg}")

# Confirmar antes de desinstalar
confirm = input("\n¿Deseas desinstalar estos paquetes? (s/n): ").strip().lower()
if confirm == "s":
    for pkg in packages_to_remove:
        try:
            # Ejecuta el comando de desinstalación
            subprocess.check_call(["pip", "uninstall", "-y", pkg])
            print(f"Paquete desinstalado: {pkg}")
        except Exception as e:
            print(f"Error al desinstalar {pkg}: {e}")
else:
    print("No se realizó ninguna acción.")
