from uteis import matematica
medida = float(input('Digite uma distância em metros: '))
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print(f'A media de {medida}m corresponde a:\n'
      '\n'
      f'\t{matematica.km(medida)} \tKm\n'
      f'\t{hm:.2f} \tHm\n'
      f'\t{dam:.1f}   \tDam\n'
      f'\t{dm:.0f}   \tDm\n'
      f'\t{cm:.0f} \tCm\n'
      f'\t{mm:.0f} \tMm\n')