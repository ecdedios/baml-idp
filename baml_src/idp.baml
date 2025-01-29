// MODELS

class Appointment {
  day_of_week string
  month string
  date int
  year int
  hour int
  minute int
  ampm string
}

class NutritionLabel {
  product string @alias("name")
  description string @description("A short description of the product")
  calories int
  fat int
  fat_ui string @description("unit per issue")
  fat_dv float @description("daily value expressed in a percentage")
  sodium int
  sodium_ui string @description("unit per issue")
  sodium_dv float @description("daily value expressed in a percentage")
  carb int
  carb_ui string @description("unit per issue")
  carb_dv float @description("daily value expressed in a percentage")
  protein int
  protein_ui string
  protein_dv float? @description("daily value expressed in a percentage")
}

// FUNCTIONS

function ExtractAppointmentFromImage(appointment_card: image) -> Appointment {
  client "openai/gpt-4o"
  prompt #"
    {{_.role("user")}}

    Extract details from this image of an appointment card reminder:
    {{ appointment_card }}

    {{ ctx.output_format }}
  "#
}

function ExtractNutritionLabelFromImage(nutrition_label: image) -> NutritionLabel {
  client "openai/gpt-4o"
  prompt #"
    {{_.role("user")}}

    Extract the name, description, and nutritional value details from this image:
    {{ nutrition_label }}

    {{ ctx.output_format }}
  "#
}

// TESTS

test Test_APPOINTMENT {
functions [ExtractAppointmentFromImage]
  args {
    appointment_card {
      url "https://baml-testing-idp-image-to-json.s3.us-east-1.amazonaws.com/appointment.jpg"
    }
  }
}

test Test_NUTRITION {
functions [ExtractNutritionLabelFromImage]
  args {
    nutrition_label {
      url "https://baml-testing-idp-image-to-json.s3.us-east-1.amazonaws.com/nutrition.jpg"
    }
  }
}
