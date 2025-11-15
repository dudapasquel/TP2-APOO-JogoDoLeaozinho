"""
Script para gerar imagens dos símbolos do jogo.
Cria imagens PNG com emojis/símbolos para usar nas roletas.
"""

from PIL import Image, ImageDraw, ImageFont
import os


def criar_simbolo(emoji: str, nome: str, cor_fundo: str = "#1a1a2e"):
    """
    Cria uma imagem PNG de um símbolo.
    
    Args:
        emoji: O emoji/símbolo a ser desenhado
        nome: Nome do arquivo (sem extensão)
        cor_fundo: Cor de fundo em hexadecimal
    """
    # Tamanho da imagem
    tamanho = (200, 200)
    
    # Criar imagem com fundo
    img = Image.new('RGBA', tamanho, cor_fundo)
    draw = ImageDraw.Draw(img)
    
    # Tentar usar uma fonte que suporte emojis
    try:
        # Windows geralmente tem Segoe UI Emoji
        font = ImageFont.truetype("seguiemj.ttf", 120)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", 120)
        except:
            font = ImageFont.load_default()
    
    # Calcular posição centralizada
    bbox = draw.textbbox((0, 0), emoji, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (tamanho[0] - w) / 2 - bbox[0]
    y = (tamanho[1] - h) / 2 - bbox[1]
    
    # Desenhar o emoji
    draw.text((x, y), emoji, font=font, fill='white', embedded_color=True)
    
    # Adicionar borda arredondada
    overlay = Image.new('RGBA', tamanho, (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    draw_overlay.rounded_rectangle(
        [(5, 5), (tamanho[0]-5, tamanho[1]-5)],
        radius=20,
        outline='#16213e',
        width=5
    )
    img = Image.alpha_composite(img, overlay)
    
    # Salvar
    caminho = os.path.join('assets', 'simbolos', f'{nome}.png')
    img.save(caminho, 'PNG')
    print(f"✓ Criado: {caminho}")


def gerar_todos_simbolos():
    """Gera todas as imagens dos símbolos do jogo."""
    print("\n🎨 Gerando imagens dos símbolos...\n")
    
    # Símbolos comuns
    simbolos_comuns = [
        ("🍒", "cereja"),
        ("🍋", "limao"),
        ("🍊", "laranja"),
        ("🍇", "uva"),
        ("🍉", "melancia"),
        ("🔔", "sino"),
        ("⭐", "estrela"),
    ]
    
    # Símbolos especiais
    simbolos_especiais = [
        ("🦁", "leao"),
        ("💎", "diamante"),
    ]
    
    # Criar símbolos comuns com fundo escuro
    for emoji, nome in simbolos_comuns:
        criar_simbolo(emoji, nome, "#1a1a2e")
    
    # Criar símbolos especiais com fundo dourado
    for emoji, nome in simbolos_especiais:
        criar_simbolo(emoji, nome, "#d4af37")
    
    # Criar símbolo de interrogação (para loading)
    criar_simbolo("❓", "loading", "#16213e")
    
    print("\n✅ Todas as imagens foram geradas com sucesso!")
    print(f"📁 Localização: assets/simbolos/\n")


if __name__ == "__main__":
    gerar_todos_simbolos()
