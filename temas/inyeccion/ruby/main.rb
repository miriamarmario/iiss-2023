# frozen_string_literal: true
require 'tk'

# Inicializar puntos de cada casa
$gryffindor_points = 0
$hufflepuff_points = 0
$ravenclaw_points = 0
$slytherin_points = 0

# Función para actualizar los puntos de una casa


# Crear ventana
root = TkRoot.new { title "Puntos de Hogwarts" }

# Crear botones para sumar y restar puntos
gryffindor_add_button = TkButton.new(root) { text "Gryffindor +1"; command {
        $gryffindor_points += 1
        gryffindor_label = TkLabel.new(root) { text "Gryffindor: #{$gryffindor_points}" }
        gryffindor_label.grid(column: 2, row: 0)

} }
gryffindor_add_button.grid(column: 0, row: 0)


griffindor_substract_button = TkButton.new(root) { text "Gryffindor -1"; command {
  $gryffindor_points -= 1
  gryffindor_label = TkLabel.new(root) { text "Gryffindor: #{$gryffindor_points}" }
  gryffindor_label.grid(column: 2, row: 0) } }
griffindor_substract_button.grid(column: 1, row: 0)


hufflepuff_add_button = TkButton.new(root) { text "Hufflepuff +1"; command {
  $hufflepuff_points += 1
  hufflepuff_label = TkLabel.new(root) { text "Hufflepuff: #{$hufflepuff_points}" }
  hufflepuff_label.grid(column: 2, row: 1) } }
hufflepuff_add_button.grid(column: 0, row: 1)


hufflepuff_substract_button = TkButton.new(root) { text "Hufflepuff -1"; command {
  $hufflepuff_points -= 1
  hufflepuff_label = TkLabel.new(root) { text "Hufflepuff: #{$hufflepuff_points}" }
  hufflepuff_label.grid(column: 2, row: 1) } }
hufflepuff_substract_button.grid(column: 1, row: 1)

ravenclaw_add_button = TkButton.new(root) { text "Ravenclaw +1"; command {
  $ravenclaw_points += 1
  ravenclaw_label = TkLabel.new(root) { text "Ravenclaw: #{$ravenclaw_points}" }
  ravenclaw_label.grid(column: 2, row: 2) } }
ravenclaw_add_button.grid(column: 0, row: 2)

ravenclaw_substract_button = TkButton.new(root) { text "Ravenclaw -1"; command {
  $ravenclaw_points -= 1
ravenclaw_label = TkLabel.new(root) { text "Ravenclaw: #{$ravenclaw_points}" }
ravenclaw_label.grid(column: 2, row: 2) } }
ravenclaw_substract_button.grid(column: 1, row: 2)


slytherin_add_button = TkButton.new(root) { text "Slytherin +1"; command {
  $slytherin_points += 1
  slytherin_label = TkLabel.new(root) { text "Slytherin: #{$slytherin_points}" }
  slytherin_label.grid(column: 2, row: 3) } }
slytherin_add_button.grid(column: 0, row: 3)

slytherin_substract_button = TkButton.new(root) { text "Slytherin -1"; command {
  $slytherin_points -= 1
  slytherin_label = TkLabel.new(root) { text "Slytherin: #{$slytherin_points}" }
  slytherin_label.grid(column: 2, row: 3) } }
slytherin_substract_button.grid(column: 1, row: 3)



# Crear
gryffindor_label = TkLabel.new(root) { text "Gryffindor: #{$gryffindor_points}" }
gryffindor_label.grid(column: 2, row: 0)

hufflepuff_label = TkLabel.new(root) { text "Hufflepuff: #{$hufflepuff_points}" }
hufflepuff_label.grid(column: 2, row: 1)

ravenclaw_label = TkLabel.new(root) { text "Ravenclaw: #{$ravenclaw_points}" }
ravenclaw_label.grid(column: 2, row: 2)

slytherin_label = TkLabel.new(root) { text "Slytherin: #{$slytherin_points}" }
slytherin_label.grid(column: 2, row: 3)

Tk.mainloop
