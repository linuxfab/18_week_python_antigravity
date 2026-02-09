
import wave
import struct
import math
import os

"""
音效生成器 (Sound Generator)
用途: 為了讓 Week 14-18 的遊戲能正常執行，我們用 Python 程式碼直接「畫」出音效檔。
不需要下載，直接執行此腳本即可生成 eat.wav 與 game_over.wav。
"""

def generate_beep(filename, duration=0.1, freq=880.0, volume=0.5):
    """ 生成一個簡單的嗶嗶聲 """
    sample_rate = 44100.0
    num_samples = int(duration * sample_rate)
    
    # 建立 wav 檔案
    output_path = os.path.join("assets", "sounds", filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with wave.open(output_path, "w") as wav_file:
        # 單聲道, 2 bytes (16-bit), 採樣率 44100
        wav_file.setparams((1, 2, int(sample_rate), num_samples, "NONE", "not compressed"))
        
        for i in range(num_samples):
            # 正弦波公式: A * sin(2 * pi * f * t)
            t = i / sample_rate
            value = int(volume * 32767.0 * math.sin(2.0 * math.pi * freq * t))
            data = struct.pack("<h", value)
            wav_file.writeframesraw(data)
            
    print(f"成功生成音效: {output_path}")

def generate_laser(filename, duration=0.5, volume=0.5):
    """ 生成一個頻率漸降的雷射聲 (適合 Game Over) """
    sample_rate = 44100.0
    num_samples = int(duration * sample_rate)
    output_path = os.path.join("assets", "sounds", filename)
    
    with wave.open(output_path, "w") as wav_file:
        wav_file.setparams((1, 2, int(sample_rate), num_samples, "NONE", "not compressed"))
        
        for i in range(num_samples):
            t = i / sample_rate
            # 頻率從 880 降到 110
            freq = 880.0 * (1.0 - t/duration) + 110.0
            value = int(volume * 32767.0 * math.sin(2.0 * math.pi * freq * t))
            data = struct.pack("<h", value)
            wav_file.writeframesraw(data)
            
    print(f"成功生成音效: {output_path}")

if __name__ == "__main__":
    print("正在準備遊戲資產...")
    # 生成吃掉音效 (高音)
    generate_beep("eat.wav", duration=0.1, freq=1200.0)
    # 生成結束音效 (下降音)
    generate_laser("game_over.wav", duration=0.8)
    print("所有基礎音效已就緒！")
