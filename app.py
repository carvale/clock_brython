from browser import document, timer, html
import datetime
from math import pi, sin, cos

class Clock:
    def __init__(self, parent_id, canvas_size, proportion, circle_width, line_color, face_color, font_color, font_style, tick_length, tick_width, h_color, m_color, s_color):
        
        self.canvas = html.CANVAS(width = canvas_size, height = canvas_size )
        document[parent_id] <= self.canvas

        self.ctx = self.canvas.getContext("2d")
        self.x, self.y = canvas_size/2, canvas_size/2
        self.radius = proportion * canvas_size
        self.circle_width = circle_width
        self.line_color = line_color
        self.face_color = face_color
        self.font_color = font_color
        self.font_style = font_style
        self.tick_lenght = tick_length
        self.tick_width = tick_width
        self.h_color = h_color
        self.m_color = m_color
        self.s_color = s_color

        self.draw_face()
        timer.set_interval(self.draw_hands, 100)

    def draw_face(self):
        self.ctx.beginPath()
        self.ctx.arc(self.x, self.y, self.radius, 0, 2 * pi)
        self.ctx.strokeStyle = self.line_color
        self.ctx.fillStyle = self.face_color
        self.ctx.lineWidth = self.circle_width
        self.ctx.fill()
        self.ctx.stroke()
        self.ctx.closePath()

        for i in range(0,60):
            angle = i * 2 * pi / 60
            if i % 5 !=0:
                self.ctx.beginPath()
                self.ctx.moveTo(self.x + self.radius * sin (angle), self.y - self.radius * cos (angle) )
                self.ctx.lineTo(self.x + (self.radius - self.tick_lenght) * sin(angle), self.y - (self.radius - self.tick_lenght) * cos (angle) )
                self.ctx.lineWidth = self.tick_width
                self.ctx.stroke()
                self.ctx.closePath()
            else:
                self.ctx.beginPath()
                self.ctx.moveTo(self.x + self.radius * sin (angle), self.y - self.radius * cos (angle) )
                self.ctx.lineTo(self.x + (self.radius - self.tick_lenght * 1.5) * sin(angle), self.y - (self.radius - self.tick_lenght * 1.5)  * cos (angle) )
                self.ctx.lineWidth = self.tick_width

                display_text = str(i//5)

                if display_text == '0':
                    display_text = '12'

                
                self.ctx.font = self.font_style
                self.ctx.fillStyle = self.font_color
                self.ctx.fillText(display_text, self.x + (self.radius - self.tick_lenght * 2.5) * sin(angle) - 6, self.y - (self.radius - self.tick_lenght * 2.5)  * cos (angle) + 6 )

                self.ctx.stroke()
                self.ctx.closePath()
        self.image_data = self.ctx.getImageData(0, 0, self.canvas.width, self.canvas.height)



    def draw_hands(self):

        self.ctx.putImageData(self.image_data, 0, 0)

        time = datetime.datetime.now()
        hour, minute, second = time.hour, time.minute, time.second
        s_angle = second * 2 * pi / 60
        m_angle = (minute + second / 60) * 2 * pi / 60
        h_angle = (hour + minute / 60 + second / 3600) * 2 * pi / 12

        self.ctx.beginPath()
        self.ctx.moveTo(self.x, self.y)
        self.ctx.lineTo(self.x + self.radius * sin(s_angle) * 0.9, self.y - self.radius * cos (s_angle) * 0.9)
        self.ctx.strokeStyle = self.s_color
        self.ctx.lineWidth = 1
        self.ctx.stroke()
        self.ctx.closePath()

        self.ctx.beginPath()
        self.ctx.moveTo(self.x, self.y)
        self.ctx.lineTo(self.x + self.radius * sin(m_angle) * 0.9, self.y - self.radius * cos (m_angle) * 0.9)
        self.ctx.strokeStyle = self.m_color
        self.ctx.lineWidth = 2
        self.ctx.stroke()
        self.ctx.closePath()

        self.ctx.beginPath()
        self.ctx.moveTo(self.x, self.y)
        self.ctx.lineTo(self.x + self.radius * sin(h_angle) * 0.7, self.y - self.radius * cos (h_angle) * 0.7)
        self.ctx.strokeStyle = self.h_color
        self.ctx.lineWidth = 6
        self.ctx.stroke()
        self.ctx.closePath()

Clock (parent_id='container', canvas_size=600, proportion=0.3, circle_width=15, 
font_color='black', font_style='20px Arial', line_color='orange', 
face_color='ivory', tick_length =15, tick_width=1, h_color='black',
 m_color='black', s_color='red')

Clock (parent_id='container', canvas_size=400, proportion=0.25, circle_width=10, 
font_color='black', font_style='20px Arial', line_color='blue', 
face_color='yellow', tick_length =15, tick_width=1, h_color='black',
 m_color='black', s_color='red')

Clock (parent_id='container', canvas_size=500, proportion=0.3, circle_width=10, 
font_color='black', font_style='15px Arial', line_color='purple', 
face_color='lavender', tick_length =10, tick_width=1, h_color='black',
 m_color='black', s_color='black')






