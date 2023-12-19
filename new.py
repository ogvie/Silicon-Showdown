Class Button:
    Method Initialize(image, pos, text_input, font, base_color, hovering_color):
        Set self.image to image
        Set self.x_pos to pos[0]
        Set self.y_pos to pos[1]
        Set self.font to font
        Set self.base_color, self.hovering_color to base_color, hovering_color
        Set self.text_input to text_input
        Set self.text to RenderText(self.text_input, self.font, self.base_color)
        If self.image is None:
            Set self.image to self.text
        Set self.rect to GetRectAtCenter(self.image, self.x_pos, self.y_pos)
        Set self.text_rect to GetRectAtCenter(self.text, self.x_pos, self.y_pos)

    Method Update(screen):
        If self.image is not None:
            Draw(self.image, self.rect, screen)
        Draw(self.text, self.text_rect, screen)

    Method CheckForInput(position):
        If position[0] in Range(self.rect.left, self.rect.right) AND position[1] in Range(self.rect.top, self.rect.bottom):
            Return True
        Return False

    Method ChangeColor(position):
        If position[0] in Range(self.rect.left, self.rect.right) AND position[1] in Range(self.rect.top, self.rect.bottom):
            Set self.text to RenderText(self.text_input, self.font, self.hovering_color)
        Else:
            Set self.text to RenderText(self.text_input, self.font, self.base_color)

