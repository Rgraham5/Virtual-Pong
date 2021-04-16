import unittest
def ball_anime():
	global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <=0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	
	#player score
	if ball.left <= 0: 
		score_time = pygame.time.get_ticks()
		player_score += 1
	
	#Opponent score
	if ball.right >= screen_width:
		score_time = pygame.time.get_ticks()
		opponent_score += 1
		
	if ball.colliderect(player) and ball_speed_x > 0:
		if abs(ball.right - player.left) < 10:
			ball_speed_x *= -1	
		elif abs(ball.bottom - player.top) < 10 or abs(ball.top - player.bottom) < 10 :
			ball_speed_y *= -1
	

	if ball.colliderect(opponent):
		if abs(ball.left - opponent.right) < 10 or abs(ball.right - player.left) < 10:
			ball_speed_x *= -1	
		else:
			ball_speed_y *= -1

class PongTestCase(unittest.TestCase):
	
	def testplayer_score(self):
	#tests for player score in Pong
		self.player_score = 0
		self.opponent_score = 0
		self.assertEqual(self.player_score, self.opponent_score, 0)




if __name__ == '__main__':
    unittest.main()