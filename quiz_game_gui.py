import pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("プログラミングクイズ")
clock = pygame.time.Clock()
font = pygame.font.Font("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 26)

# プログラミングクイズ（解説付き）
quizzes = [
    {
        "question": "次のコードの出力は？\nprint(1 + 1)",
        "answer": "2",
        "explain": "1 + 1 は 2 です。"
    },
    {
        "question": "次のコードの出力は？\nprint(len('hello'))",
        "answer": "5",
        "explain": "文字列 'hello' は 5 文字です。"
    },
    {
        "question": "次のコードの出力は？\nprint(3 * 2)",
        "answer": "6",
        "explain": "3 × 2 = 6 です。"
    },
    {
        "question": "次のコードの出力は？\nprint('A'.lower())",
        "answer": "a",
        "explain": "lower() メソッドは文字を小文字に変換します。"
    },
    {
        "question": "次のコードの出力は？\nprint(10 // 3)",
        "answer": "3",
        "explain": "// は切り捨て除算。10 ÷ 3 = 3 余り 1 → 3 が出力されます。"
    }
]

quiz_index = 0
score = 0
user_text = ""
show_feedback = False
feedback_color = (0, 255, 0)
feedback_start_time = 0
feedback_text = []

running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not show_feedback:
                # Enterキー（Windows対応）
                if event.key == pygame.K_RETURN or event.key == 1073741912:
                    if quiz_index < len(quizzes):
                        correct = user_text.strip() == quizzes[quiz_index]["answer"]
                        if correct:
                            score += 1
                            feedback_color = (0, 255, 0)
                            feedback_text = [f"正解: {quizzes[quiz_index]['answer']}"]
                        else:
                            feedback_color = (255, 0, 0)
                            feedback_text = [
                                f"正解: {quizzes[quiz_index]['answer']}",
                                f"解説: {quizzes[quiz_index]['explain']}"
                            ]

                        show_feedback = True
                        feedback_start_time = current_time
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if event.unicode.isprintable():
                        user_text += event.unicode

    screen.fill((0, 0, 0))

    if quiz_index < len(quizzes):
        # 問題表示
        lines = quizzes[quiz_index]["question"].split("\n")
        for i, line in enumerate(lines):
            screen.blit(font.render(line, True, (255, 255, 255)), (50, 50 + i * 35))

        if show_feedback:
            for i, line in enumerate(feedback_text):
                screen.blit(font.render(line, True, feedback_color if i == 0 else (200, 200, 200)), (50, 150 + i * 35))
            if current_time - feedback_start_time >= 1500:  # 1.5秒待機
                quiz_index += 1
                user_text = ""
                show_feedback = False
        else:
            display_text = user_text if user_text else "_"
            screen.blit(font.render("答え: " + display_text, True, (255, 255, 0)), (50, 150))
    else:
        # 全問終了
        screen.fill((0, 0, 0))
        screen.blit(font.render(f"ゲーム終了！スコア: {score}/{len(quizzes)}", True, (0, 255, 0)), (50, 50))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
