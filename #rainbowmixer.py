#RainbowMixerRGB
import flet as ft

def main(page: ft.Page):
    page.title = " Color Mixer of RG&B"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.bgcolor = "#000000"

    slider_r = ft.Slider(min=0, max=255, divisions=255, value=0, label="{value}", active_color=ft.colors.RED)
    slider_g = ft.Slider(min=0, max=255, divisions=255, value=0, label="{value}", active_color=ft.colors.GREEN)
    slider_b = ft.Slider(min=0, max=255, divisions=255, value=0, label="{value}", active_color=ft.colors.BLUE)

    rgb_text = ft.Text("RGB: (0, 0, 0)", size=20)
    hex_text = ft.Text("HEX: #000000", size=20)

    def update_color(e):
        r = int(slider_r.value)
        g = int(slider_g.value)
        b = int(slider_b.value)
        hex_color = f"#{r:02x}{g:02x}{b:02x}"

      
        page.bgcolor = hex_color
        rgb_text.value = f"RGB: ({r}, {g}, {b})"
        hex_text.value = f"HEX: {hex_color.upper()}"
        page.update()

    slider_r.on_change = update_color
    slider_g.on_change = update_color
    slider_b.on_change = update_color

    page.add(
        ft.Text("Move the sliders to mix the colors and see what happens!", size=24, weight="bold"),
        ft.Text("Red", color=ft.colors.RED),
        slider_r,
        ft.Text("Green", color=ft.colors.GREEN),
        slider_g,
        ft.Text("Blue", color=ft.colors.BLUE),
        slider_b,
        rgb_text,
        hex_text
    )

    update_color(None)

ft.app(target=main)
