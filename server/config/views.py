from django.http import HttpResponse

default_home_ui = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dafy - Secondhand Marketplace</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #FFF8F0 0%, #FFE4D6 100%);
      color: #333;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    
    header {
      background-color: rgba(255, 255, 255, 0.9);
      padding: 20px 40px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.05);
      position: sticky;
      top: 0;
      z-index: 100;
    }
    
    header a {
      color: #FF7F50;
      text-decoration: none;
      font-size: 14px;
      font-weight: 500;
      transition: color 0.3s;
    }
    
    header a:hover {
      color: #FF6347;
    }
    
    .container {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 40px 20px;
      text-align: center;
      max-width: 900px;
      margin: 0 auto;
    }
    
    .logo {
      font-weight: 600;
      font-size: 72px;
      color: #FF7F50;
      margin-bottom: 20px;
      text-shadow: 2px 2px 4px rgba(255, 127, 80, 0.2);
    }
    
    .tagline {
      font-size: 20px;
      color: #666;
      margin-bottom: 40px;
      font-weight: 400;
    }
    
    .description {
      font-size: 16px;
      line-height: 1.8;
      color: #555;
      margin-bottom: 30px;
      max-width: 700px;
    }
    
    .features {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 30px;
      margin-top: 40px;
      width: 100%;
    }
    
    .feature {
      background: rgba(255, 255, 255, 0.7);
      padding: 25px;
      border-radius: 15px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    .feature-icon {
      font-size: 36px;
      color: #FF7F50;
      margin-bottom: 15px;
    }
    
    .feature-title {
      font-size: 18px;
      font-weight: 600;
      color: #333;
      margin-bottom: 10px;
    }
    
    .feature-text {
      font-size: 14px;
      color: #666;
      line-height: 1.6;
    }
    
    footer {
      background-color: rgba(255, 255, 255, 0.9);
      padding: 30px 40px;
      text-align: center;
      box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }
    
    .social-icons {
      display: flex;
      justify-content: center;
      gap: 25px;
      margin-bottom: 20px;
    }
    
    .social-icons a {
      color: #FF7F50;
      font-size: 24px;
      transition: transform 0.3s, color 0.3s;
      text-decoration: none;
    }
    
    .social-icons a:hover {
      transform: translateY(-3px);
      color: #FF6347;
    }
    
    .copyright {
      font-size: 12px;
      color: #999;
    }
  </style>
</head>
<body>
  
  <header>
    <a href="https://www.facebook.com/nischal.pokharel.598234" target="_blank">Nischal: Backend DRF Developer</a>
  </header>
  
  <div class="container">
    <div class="logo">Dafy.</div>
    
    <div class="tagline">Buy. Sell. Connect.</div>
    
    <div class="description">
      Dafy is your trusted platform for buying and selling secondhand products with ease. 
      Connect directly with buyers and sellers in your community, communicate seamlessly, 
      and discover amazing deals on pre-loved items. From electronics to furniture, 
      fashion to books—give products a second life while building meaningful connections.
    </div>
    
    <div class="features">
      <div class="feature">
        <div class="feature-icon">🛍️</div>
        <div class="feature-title">Easy Listing</div>
        <div class="feature-text">Post your items in seconds with photos and descriptions</div>
      </div>
      
      <div class="feature">
        <div class="feature-icon">💬</div>
        <div class="feature-title">Direct Chat</div>
        <div class="feature-text">Communicate directly with buyers and sellers in real-time</div>
      </div>
      
      <div class="feature">
        <div class="feature-icon">🤝</div>
        <div class="feature-title">Safe Marketplace</div>
        <div class="feature-text">Trusted community of verified users buying and selling locally</div>
      </div>
    </div>
  </div>
  
  <footer>
    <div class="social-icons">
      <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
      <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
      <a href="#" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
      <a href="#" aria-label="X (Twitter)"><i class="fab fa-x-twitter"></i></a>
    </div>
    <div class="copyright">© 2026 Dafy. All rights reserved.</div>
  </footer>

</body>
</html>

"""

def defaultscreen(request):
    return HttpResponse(default_home_ui)