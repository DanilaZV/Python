from hookah import Hookah
import restoran

Borsch = restoran.Restoran(1, 'большая', 'Русской', 250, 40)
Borsch.zakaz()
Borsch.posadka()
Borsch.employees()
Borsch.time_work(10)

Pchel = Hookah(1, 'Большой', 'Русская', 250, 40)
Pchel.virginia.order_hook()
Pchel.prosto()