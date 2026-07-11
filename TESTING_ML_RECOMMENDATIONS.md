# Testing ML-Powered Recommendations

## Quick Test Guide

### 1. Start the Application

Both servers should already be running:
- **Frontend**: http://localhost:3000/
- **Backend**: http://127.0.0.1:8000/

### 2. Create a New User Account

1. Go to http://localhost:3000/
2. Click "Sign Up" or "Get Started"
3. Fill in your details:
   - Email: test@example.com
   - Password: testpass123
   - Name: Test User
4. Complete the signup

### 3. Set Your Preferences

After signup, you'll be prompted to set preferences:

1. **Budget Range**:
   - Min: 5,000,000 PKR
   - Max: 10,000,000 PKR

2. **Property Requirements**:
   - Bedrooms: 3
   - Bathrooms: 2
   - Property Type: House, Flat

3. **Preferred Locations**:
   - Add: "DHA"
   - Add: "Bahria"
   - Add: "Fazaia"

4. **Amenity Importance** (0-1 scale):
   - Schools: 0.9 (Very Important)
   - Hospitals: 0.8 (Important)
   - Metro: 0.5 (Moderate)
   - Parks: 0.6 (Moderate)
   - Shopping: 0.7 (Important)
   - Restaurants: 0.5 (Moderate)

5. Click "Save Preferences"

### 4. View ML Recommendations

1. Go to the Dashboard
2. You should see "Property Recommendations" section
3. Properties will be displayed with:
   - **ML Score**: 0-10 (higher is better match)
   - **Match Percentage**: 0-99%
   - **ROI Predictions**: 1-year and 5-year estimates

### 5. Verify ML is Working

**Before the fix:**
- All properties had the same score (0.5)
- Recommendations were essentially random
- No personalization based on preferences

**After the fix:**
- Properties have different scores (e.g., 10.0, 9.45, 8.23)
- Top recommendations match your preferences:
  - Within or close to your budget
  - In your preferred locations
  - Have the amenities you prioritized
- Scores reflect how well each property matches your needs

### 6. Check Browser Console

Open Developer Tools (F12) and check the Console:

```javascript
// You should see logs like:
ML Recommendations: [
  {
    property: { id: 123, title: "...", location: "DHA Phase 5", ... },
    score: 9.45,
    match_percentage: 94,
    roi_1yr: 12.5,
    roi_5yr: 45.2
  },
  ...
]
```

### 7. Test Different Preferences

Try changing your preferences to see how recommendations adapt:

1. Go to Profile → Preferences
2. Change budget to 15,000,000 - 20,000,000
3. Change location to "Gulberg"
4. Save and return to Dashboard
5. Recommendations should update to match new preferences

## API Testing (Optional)

### Using curl or Postman

1. **Login to get JWT token**:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'
```

2. **Get Recommendations**:
```bash
curl -X GET "http://127.0.0.1:8000/api/properties/recommendations/?limit=10" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

3. **Expected Response**:
```json
{
  "count": 10,
  "properties": [
    {
      "property": {
        "id": 16660,
        "title": "Beautiful House in DHA",
        "location": "DHA Phase 5, Islamabad",
        "price": "8500000.00",
        "bedrooms": 3,
        "bathrooms": 2,
        "area_sqft": 2500,
        "school_score": 0.85,
        "hospital_score": 0.72,
        ...
      },
      "score": 9.45,
      "match_percentage": 94,
      "roi_1yr": 12.5,
      "roi_5yr": 45.2
    },
    ...
  ]
}
```

## Understanding the Scores

### ML Score (0-10)
- **9-10**: Excellent match - highly recommended
- **7-9**: Good match - meets most criteria
- **5-7**: Fair match - meets some criteria
- **0-5**: Poor match - doesn't align well with preferences

### Match Percentage (0-99%)
- Derived from ML score: `min(score * 10, 99)`
- Easy-to-understand metric for users

### ROI Predictions
- **1-year ROI**: Expected return in first year (%)
- **5-year ROI**: Expected cumulative return over 5 years (%)
- Based on historical data and market trends

## What the ML Model Considers

The XGBoost model evaluates 11 features:

1. **Price Fit Score**: How well the price matches your budget
2. **Bedroom Match**: Meets your bedroom requirements
3. **Area Match**: Property size preferences
4. **Location Match**: In your preferred locations
5. **School Score**: Proximity to schools (weighted by importance)
6. **Hospital Score**: Proximity to hospitals (weighted by importance)
7. **Metro Score**: Proximity to metro (weighted by importance)
8. **Park Score**: Proximity to parks (weighted by importance)
9. **Facility Match Ratio**: Overall amenity availability
10. **Risk-Adjusted Safety**: Area safety score
11. **Risk-Adjusted ROI**: Investment potential

## Troubleshooting

### No Recommendations Showing
1. Check if you're logged in
2. Verify preferences are saved (Profile → Preferences)
3. Check browser console for errors
4. Verify backend is running (http://127.0.0.1:8000/)

### All Scores are 0.5
- This means ML model isn't being used (fallback mode)
- Check backend logs for errors
- Verify ML models are loaded (check startup logs)

### Backend Errors
1. Check backend terminal for error messages
2. Verify database has properties: `python manage.py shell -c "from apps.properties.models import Property; print(Property.objects.count())"`
3. Run test script: `python test_recommendations.py`

## Success Indicators

✅ Different properties have different scores
✅ Top recommendations are in your preferred locations
✅ Prices are within or close to your budget
✅ Properties have high scores for amenities you prioritized
✅ Changing preferences updates recommendations
✅ ROI predictions are displayed

## Next Steps

1. **Explore Properties**: Click on recommended properties to see details
2. **Adjust Preferences**: Fine-tune your preferences for better matches
3. **Compare Properties**: Use ML scores to compare similar properties
4. **Track ROI**: Monitor ROI predictions for investment decisions
