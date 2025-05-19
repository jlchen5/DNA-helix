import time
import os
import sys
from random import randint
from colorama import Fore, init

# 初始化颜色支持[3](@ref)
init(autoreset=True)
COLORS = {
    'A': Fore.RED,
    'T': Fore.GREEN,
    'G': Fore.YELLOW,
    'C': Fore.BLUE,
    '-': Fore.WHITE
}

def clear_console():
    """ 更流畅的终端清屏方法 """
    print('\033[2J\033[H', end='')

def print_dna(length=20, delay=0.08):
    """ 增强版DNA动画 """
    # 扩展的ASCII艺术模板[4](@ref)
    patterns = [
        ["A-----T", "■    ■"], 
        [" T---A ", "  ■■■  "],
        ["  G-G  ", "   ◈   "],
        ["   C   ", "   ▲   "],
        # 更多动态元素...
    ]
    
    wave_phase = 0  # 波浪效果相位
    frame_counter = 0
    
    try:
        while True:
            wave_phase = (wave_phase + 1) % 4
            for offset in range(len(patterns[0])):
                clear_console()
                # 动态参数生成[7](@ref)
                dynamic_offset = int(2 * abs(wave_phase - 2))
                for line in range(length):
                    # 波浪形变动画[2,7](@ref)
                    wave_offset = (dynamic_offset + line) % 4
                    pattern = patterns[(frame_counter + line + wave_offset) % len(patterns)]
                    
                    # 彩色渲染与动态间距[3,6](@ref)
                    colored_line = ""
                    for char in pattern[offset % len(pattern)]:
                        colored_char = COLORS.get(char, Fore.WHITE) + char
                        # 添加随机粒子特效[2](@ref)
                        if randint(0, 20) == 1:  
                            colored_char = Fore.CYAN + '*' + Fore.RESET
                        colored_line += colored_char
                    
                    # 3D立体效果[4](@ref)
                    indent = " " * abs(line - length//2)
                    print(f"{indent}{colored_line}")
                
                time.sleep(delay * (1 + 0.2 * (offset % 2)))  # 动态帧率[5](@ref)
                frame_counter += 1
    except KeyboardInterrupt:
        print("\nDNA序列模拟已终止")

if __name__ == "__main__":
    print_dna(20, 0.08)
