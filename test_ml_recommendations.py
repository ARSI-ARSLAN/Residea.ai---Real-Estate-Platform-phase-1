"""
Quick test to verify ML recommendations are working
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_ml_health():
    """Test ML models are loaded"""
    print("=" * 60)
    print("Testing ML Health Check...")
    print("=" * 60)
    
    response = requests.get(f"{BASE_URL}/api/ml/health/")
    data = response.json()
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(data, indent=2)}")
    
    if data.get('models_loaded') and data.get('status') == 'healthy':
        print("✅ ML Models are loaded and healthy!")
        return True
    else:
        print("❌ ML Models are not loaded properly")
        return False

def test_recommendations():
    """Test recommendations endpoint"""
    print("\n" + "=" * 60)
    print("Testing ML Recommendations...")
    print("=" * 60)
    
    # Test without user preferences (fallback)
    response = requests.get(f"{BASE_URL}/api/properties/recommendations/?limit=5")
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Recommendations Count: {data.get('count', 0)}")
        
        if data.get('properties'):
            print("\nTop 3 Recommendations:")
            for i, rec in enumerate(data['properties'][:3], 1):
                prop = rec.get('property', {})
                print(f"\n{i}. {prop.get('title', 'N/A')}")
                print(f"   Location: {prop.get('location', 'N/A')}")
                price = prop.get('price', 0)
                try:
                    price_float = float(price) if price else 0
                    print(f"   Price: ${price_float:,.2f}")
                except:
                    print(f"   Price: {price}")
                print(f"   ML Score: {rec.get('score', 0):.2f}/10")
                print(f"   Match: {rec.get('match_percentage', 0)}%")
                print(f"   ROI (1yr): {rec.get('roi_1yr', 0):.2f}%")
                print(f"   ROI (5yr): {rec.get('roi_5yr', 0):.2f}%")
            
            print("\n✅ Recommendations are working!")
            return True
        else:
            print("⚠️  No properties returned (database might be empty)")
            return False
    else:
        print(f"❌ Error: {response.text}")
        return False

def test_properties_count():
    """Check how many properties are in the database"""
    print("\n" + "=" * 60)
    print("Checking Properties Database...")
    print("=" * 60)
    
    response = requests.get(f"{BASE_URL}/api/properties/")
    
    if response.status_code == 200:
        data = response.json()
        count = data.get('count', 0)
        print(f"Total Properties: {count}")
        
        if count > 0:
            print("✅ Properties database is populated")
            return True
        else:
            print("⚠️  No properties in database")
            print("   Run: python manage.py load_properties")
            return False
    else:
        print(f"❌ Error accessing properties: {response.text}")
        return False

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  RESIDEA.AI ML RECOMMENDATIONS TEST")
    print("=" * 60)
    print(f"Testing against: {BASE_URL}")
    print()
    
    try:
        # Test 1: ML Health
        ml_healthy = test_ml_health()
        
        # Test 2: Properties Count
        has_properties = test_properties_count()
        
        # Test 3: Recommendations
        recs_working = test_recommendations()
        
        # Summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"ML Models Loaded: {'✅' if ml_healthy else '❌'}")
        print(f"Properties Available: {'✅' if has_properties else '⚠️'}")
        print(f"Recommendations Working: {'✅' if recs_working else '❌'}")
        
        if ml_healthy and recs_working:
            print("\n🎉 SUCCESS! ML recommendations are fully operational!")
        elif ml_healthy and not has_properties:
            print("\n⚠️  ML models are loaded but no properties in database")
            print("   Load properties using: python manage.py load_properties")
        else:
            print("\n❌ Some tests failed. Check the output above.")
            
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to backend server")
        print("   Make sure the backend is running on http://localhost:8000")
        print("   Run: start_backend.bat")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
