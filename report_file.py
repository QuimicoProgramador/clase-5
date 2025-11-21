import total_usd
report_file = "daily_report.txt"

data_to_write = f"Reporte de Ejecución\nVolumen Total USD: {total_usd}\nEstado: Completado"

with open(report_file, 'w', encoding='utf-8') as f:
    f.write(data_to_write)

print(f"✅ Reporte guardado en {report_file}")